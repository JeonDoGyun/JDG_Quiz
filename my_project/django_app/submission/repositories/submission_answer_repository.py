from ..models.submission_answer import SubmissionAnswer
from django.db.models import QuerySet


class SubmissionAnswerRepository:
    def get_by_submission(self, submission_answer_id: str) -> QuerySet:
        return SubmissionAnswer.objects.filter(submission_answer_id=submission_answer_id)

    def save(self, answer: SubmissionAnswer) -> SubmissionAnswer:
        answer.save()
        return answer

    def bulk_save(self, answers: list[SubmissionAnswer]) -> list[SubmissionAnswer]:
        SubmissionAnswer.objects.bulk_create(answers)
        return answers
