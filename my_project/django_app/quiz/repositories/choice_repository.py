from django.db.models import QuerySet
from ..models.choice import Choice


class ChoiceRepository:
    def get_choices_by_question(self, question_id: str) -> QuerySet:
        return Choice.objects.filter(question_id=question_id)

    def get_choice_by_id(self, choice_id: str) -> Choice:
        return Choice.objects.get(id=choice_id)

    def save_choice(self, choice: Choice) -> Choice:
        choice.save()
        return choice

    def delete_choice(self, choice_id: str) -> None:
        Choice.objects.filter(id=choice_id).delete()
