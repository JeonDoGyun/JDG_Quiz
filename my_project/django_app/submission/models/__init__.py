# Django ORM 등록
# import os
# import django
# from django.core.exceptions import AppRegistryNotReady

# # Django 환경 설정 로드
# if not os.environ.get("DJANGO_SETTINGS_MODULE"):
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# # Django가 로드되지 않은 경우 실행
# try:
#     from django.apps import apps
#     apps.check_apps_ready()
# except AppRegistryNotReady:
#     django.setup()

from .submission_answer import SubmissionAnswer
from .submission import Submission