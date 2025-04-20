from django.core.exceptions import ObjectDoesNotExist, ValidationError

from ..models.choice import Choice
from ..repositories.choice_repository import ChoiceRepository


class ChoiceService:
    def __init__(self, choice_repository: ChoiceRepository = ChoiceRepository()):
        self.choice_repository = choice_repository

    def create_choice(self, choice: Choice) -> Choice:
        return self.choice_repository.save_choice(choice)

    def update_choice(self, choice: Choice) -> Choice:
        try:
            existing = self.choice_repository.get_choice_by_id(choice.id)
        except ObjectDoesNotExist:
            raise ValidationError("해당 보기 항목이 존재하지 않습니다. update 실패")

        return self.choice_repository.save_choice(choice)

    def delete_choice(self, choice_id: str) -> None:
        self.choice_repository.delete_choice(choice_id)

    def get_choices_by_question(self, question_id: str):
        return self.choice_repository.get_choices_by_question(question_id)

    def add_choices_to_question(self, choices: list[Choice]) -> list[Choice]:
        if len(choices) < 3:
            raise ValidationError("선택지는 최소 3개 이상이어야 합니다.")

        # 정답 개수가 반드시 1개는 있어야 함
        num_correct = [choice.is_answer for choice in choices].count(True)
        if num_correct != 1:
            raise ValidationError("정답은 정확히 1개여야 합니다.")

        for choice in choices:
            self.choice_repository.save_choice(choice)

        return choices
