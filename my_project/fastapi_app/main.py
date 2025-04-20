import os
import django
from django.core.exceptions import AppRegistryNotReady

from .docs.openapi_utils import custom_openapi


# Django 환경 설정 로드
if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "django_app.config.settings")

# Django가 로드되지 않은 경우 실행
try:
    from django.apps import apps
    apps.check_apps_ready()
except AppRegistryNotReady:
    django.setup()

from fastapi import FastAPI
from .routers.controllers import quiz_controller
from .routers.controllers import submission_controller


app = FastAPI(
    title="FastAPI 기반 사용자 API",
    description="""
    DRF Swagger 문서: [여기서 확인](http://localhost/internal/drf-docs)
    🧠 이 [페이지](http://localhost/public/docs)는 FastAPI Swagger 문서입니다.
    """
)

app.include_router(quiz_controller.router)
app.include_router(submission_controller.router)

app.openapi = lambda: custom_openapi(app)
