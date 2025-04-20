from datetime import datetime

from ...quiz.repositories.choice_repository import ChoiceRepository
from ...quiz.repositories.question_repository import QuestionRepository
from ...quiz.repositories.quiz_repository import QuizRepository

from ..models.submission_answer import SubmissionAnswer
from ..models.submission import Submission
from ..services.snapshot_generator import SnapshotGenerator
from ..services.score_grader import ScoreGrader
from ..repositories.submission_answer_repository import SubmissionAnswerRepository
from ..repositories.submission_repository import SubmissionRepository


class SubmissionService:
    submission_repository = SubmissionRepository()
    quiz_repository = QuizRepository()
    question_repository = QuestionRepository()
    choice_repository = ChoiceRepository()
    submission_answer_repository = SubmissionAnswerRepository()
    snapshot_generator = SnapshotGenerator()
    score_grader = ScoreGrader()

    def get_submission_by_id(self, submission_id: str) -> Submission:
        return self.submission_repository.get_submission_by_id(submission_id)

    # 시험 응시 만들기
    def create_submission(self, user_id: str, quiz_id: int) -> Submission:
        # 응시가 있으면 응시 기록(문제와 선택한 답변)을 반환
        existing = self.submission_repository.get_submission_by_user_and_quiz(
            user_id, quiz_id)
        if existing:
            return existing

        quiz = self.quiz_repository.get_quiz_by_id(quiz_id)
        all_questions = self.question_repository.get_questions_by_quiz(quiz_id)
        all_choices = [
            choice
            for question in all_questions
            for choice in self.choice_repository.get_choices_by_question(question.id)
        ]

        # snapshot 생성 (랜덤 추출 및 랜덤 배치 적용)
        question_snapshots = self.snapshot_generator.generate(
            quiz=quiz,
            all_questions=all_questions,
            all_choices=all_choices,
        )

        # Submission 객체 생성 및 저장
        submission = Submission.objects.create(
            user_id=user_id,
            quiz_id=quiz.quiz_id,
            created_at=datetime.now(),
        )

        # SubmissionAnswer 목록 생성 및 저장
        answers = [
            SubmissionAnswer(
                submission=submission,
                question_id=qs["question_id"],
                choice_snapshot=qs["choices"],
                created_at=datetime.now(),
            )
            for qs in question_snapshots
        ]

        self.submission_answer_repository.bulk_save(answers)

        return submission

    # 답안 제출 + 채점
    def submit_answers(self, submission: Submission, user_id: str, answers_data: list[dict]) -> Submission:
        if str(submission.user_id) != str(user_id):
            raise PermissionError("You do not have access to this submission.")

        # 채점하기
        result = self.score_grader.grade(answers_data)

        answers = []
        for answer_data in answers_data:
            selected_choice_id = answer_data["selected_choice_id"]
            is_correct = result.is_correct_map[selected_choice_id]

            answers.append(
                SubmissionAnswer(
                    submission=submission,
                    question_id=answer_data["question_id"],
                    selected_choice_id=selected_choice_id,
                    is_correct=is_correct,
                    created_at=datetime.now()
                )
            )

        self.submission_answer_repository.bulk_save(answers)

        submission.score = result.score  # 맞은 개수
        submission.submitted_at = datetime.now()

        return self.submission_repository.save_submission(submission)

    # 응시 결과 조회
    def get_submission_result(self, submission_id: str, user_id: str) -> Submission:
        submission = self.submission_repository.get_submission_by_id(
            submission_id)
        if not submission:
            raise ValueError("Submission not found")

        if str(submission.user_id) != str(user_id):
            raise PermissionError("You do not have access to this submission.")

        return submission
