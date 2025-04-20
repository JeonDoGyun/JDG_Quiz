from django.db.models import QuerySet
from ..models.question import Question


class QuestionRepository:
    def get_questions_by_quiz(self, quiz_id: str) -> QuerySet:
        return Question.objects.filter(quiz_id=quiz_id)

    def get_question_by_id(self, question_id: str) -> Question:
        return Question.objects.get(id=question_id)

    def save_question(self, question: Question) -> Question:
        question.save()
        return question

    def delete_question(self, question_id: str) -> None:
        Question.objects.filter(id=question_id).delete()
