from datetime import datetime

from ..models.submission_answer import SubmissionAnswer
from ..models.submission import Submission
from ..services.snapshot_generator import SnapshotGenerator
from ..services.score_grader import ScoreGrader
from ..repositories.submission_answer_repository import SubmissionAnswerRepository
from ..repositories.submission_repository import SubmissionRepository


class SubmissionService:
    submission_repository = SubmissionRepository()
    submission_answer_repository = SubmissionAnswerRepository()
    snapshot_generator = SnapshotGenerator()
    score_grader = ScoreGrader()

    def create_submission(self, quiz, user) -> Submission:
        snapshot = self.snapshot_generator.generate(quiz)

        submission = Submission(
            quiz=quiz, user=user, snapshot=snapshot
        )

        return self.submission_repository.save_submission(submission)

    def submit_answers(self, submission: Submission, answers_data: list[dict]) -> Submission:
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
                    is_correct=is_correct
                )
            )

        self.submission_answer_repository.bulk_save(answers)
        submission.score = result.score  # 맞은 개수
        submission.submitted_at = datetime.now()

        return self.submission_repository.save_submission(submission)
