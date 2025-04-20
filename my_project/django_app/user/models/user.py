import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

from ..permissions.roles import Role


class User(AbstractUser):
    role = models.CharField(
        max_length=10,
        choices=[(r.value, r.name) for r in Role],
        default=Role.USER.value
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "users"
