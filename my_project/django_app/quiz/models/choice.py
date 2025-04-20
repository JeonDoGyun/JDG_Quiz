import uuid
from django.db import models
from .question import Question


class Choice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField(max_length=500)
    is_answer = models.BooleanField(default=False)

    class Meta:
        db_table = 'choices'
