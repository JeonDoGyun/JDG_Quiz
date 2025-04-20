from django.core.exceptions import ObjectDoesNotExist, ValidationError

from ..models.question import Question
from ..repositories.question_repository import QuestionRepository


class QuestionService:
    def __init__(self, question_repository: QuestionRepository):
        self.question_repository = question_repository

    def create_question(self, question: Question) -> Question:
        return self.question_repository.save_question(question)

    def update_question(self, new_question_data: Question) -> Question:
        try:
            existing = self.question_repository.get_question_by_id(
                new_question_data.id)
        except ObjectDoesNotExist:
            raise ValidationError("해당 질문이 존재하지 않습니다. update 실패")

        return self.question_repository.save_question(new_question_data)

    def delete_question(self, question_id: str) -> None:
        self.question_repository.delete_question(question_id)

    def get_questions_by_quiz(self, quiz_id: str):
        return self.question_repository.get_questions_by_quiz(quiz_id)
