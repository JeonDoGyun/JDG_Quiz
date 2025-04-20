from dataclasses import dataclass

from quiz.repositories.choice_repository import ChoiceRepository


@dataclass
class GradingResult:
    is_correct_map: dict[str, bool]  # selected_choice_id, is_correct
    score: int


class ScoreGrader:
    choice_repository = ChoiceRepository()

    # 선택지에 대한 정답 여부와 정답 개수 return
    def grade(self, answers_data: list[dict]) -> GradingResult:
        correct_answer = 0
        is_correct_map = {}

        for answer_data in answers_data:
            selected_choice_id = answer_data["selected_choice_id"]
            selected_choice = self.choice_repository.get_choice_by_id(
                selected_choice_id)
            is_correct = selected_choice.is_answer

            is_correct_map[selected_choice_id] = is_correct

            if is_correct:
                correct_answer += 1

        return GradingResult(
            is_correct_map=is_correct_map,
            score=correct_answer
        )
