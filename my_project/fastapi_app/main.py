import os
import django
from django.core.exceptions import AppRegistryNotReady


# Django 환경 설정 로드
if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Django가 로드되지 않은 경우 실행
try:
    from django.apps import apps
    apps.check_apps_ready()
except AppRegistryNotReady:
    django.setup()

from fastapi import FastAPI
from .controllers import quiz_controller

app = FastAPI(
    title="Assignment about Quiz API",
)

quiz_router = quiz_controller.router
app.include_router(quiz_router)
