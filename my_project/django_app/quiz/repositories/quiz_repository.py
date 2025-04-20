from django.db.models import QuerySet
from ..models.quiz import Quiz


class QuizRepository:
    def get_all_quizzes(self) -> QuerySet:
        return Quiz.objects.all()

    def get_quiz_by_id(self, quiz_id: str) -> Quiz:
        return Quiz.objects.get(id=quiz_id)

    def save_quiz(self, quiz: Quiz) -> Quiz:
        quiz.save()
        return quiz

    def delete_quiz(self, quiz_id: str) -> None:
        Quiz.objects.filter(id=quiz_id).delete()
