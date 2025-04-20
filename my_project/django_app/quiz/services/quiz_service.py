from django.core.exceptions import ObjectDoesNotExist, ValidationError

from ..models.question import Question
from ..models.quiz import Quiz
from ..repositories.quiz_repository import QuizRepository


class QuizService:
    def __init__(self, quiz_repository: QuizRepository):
        self.quiz_repository = quiz_repository

    def create_quiz(self, quiz: Quiz) -> Quiz:
        return self.quiz_repository.save_quiz(quiz)

    def update_quiz(self, new_quiz_data: Quiz) -> Quiz:
        try:
            quiz = self.quiz_repository.get_quiz_by_id(new_quiz_data.quiz_id)
        except ObjectDoesNotExist:
            raise ValidationError("해당 ID의 퀴즈가 존재하지 않습니다.")

        return self.quiz_repository.save_quiz(new_quiz_data)

    def delete_quiz(self, quiz_id):
        self.quiz_repository.delete_quiz(quiz_id)
