from django.urls import path
from submission.views.submission_view import SubmissionSubmitView

urlpatterns = [
    # 응시 내용 제출 + 결과 확인
    path('<uuid:submission_id>/submit/',
         SubmissionSubmitView.as_view(), name='submission-submit'),
]
