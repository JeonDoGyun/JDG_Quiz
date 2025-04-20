import uuid
from django.db import models
from django.conf import settings


class Quiz(models.Model):
    quiz_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    number_of_questions = models.PositiveIntegerField()
    page_size = models.PositiveIntegerField()
    is_randomised_questions = models.BooleanField(default=False)
    is_randomised_choices = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="quizzes"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'quizzes'
