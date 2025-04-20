import uuid
from django.db import models
from django.conf import settings
from quiz.models.quiz import Quiz


class Submission(models.Model):
    quiz_submission_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="submissions")
    quiz_id = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name="submissions")

    # 문제 및 보기 랜덤 배치 snapshot
    snapshot = models.JSONField()

    score = models.PositiveIntegerField()  # 채점 완료 후 저장
    submitted_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = "submissions"
