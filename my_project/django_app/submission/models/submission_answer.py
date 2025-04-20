# 응시한 사용자가 입력한 답안
import uuid
from django.db import models

from ...quiz.models.question import Question
from ...quiz.models.choice import Choice
from .submission import Submission


class SubmissionAnswer(models.Model):
    submission_answer_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    quiz_submission_id = models.ForeignKey(
        Submission, on_delete=models.CASCADE, related_name="answers")
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice_id = models.ForeignKey(Choice, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    class Meta:
        db_table = "submission_answers"
