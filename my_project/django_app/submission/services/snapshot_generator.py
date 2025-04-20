import random

from ...quiz.models.quiz import Quiz
from ...quiz.repositories.choice_repository import ChoiceRepository
from ...quiz.repositories.question_repository import QuestionRepository


class SnapshotGenerator:
    question_repository = QuestionRepository()
    choice_repository = ChoiceRepository()

    # 랜덤하게 섞인 문제의 snapshot 만들기
    def generate(self, quiz: Quiz) -> list[dict]:
        questions = list(
            self.question_repository.get_questions_by_quiz(quiz.quiz_id))
        if quiz.is_randomised_questions:  # 문제 random 허용을 선택한 경우
            random.shuffle(questions)

        # 관리자가 지정한 출제 문제 수만큼 가져오기
        selected_randomised_questions = questions[:quiz.number_of_questions]

        snapshot = []
        for question in selected_randomised_questions:
            choices = list(self.choice_repository.get_choices_by_question(
                question.question_id))
            if quiz.is_randomised_choices:  # 선택지 random 허용을 선택한 경우
                random.shuffle(choices)

            snapshot.append({
                "question_id": question.question_id,
                "content": question.description,
                "choices": [
                    {"choice_id": str(choice.id), "text": choice.text}
                    for choice in choices
                ]
            })

        return snapshot
