from django_app.submission.services.submission_service import SubmissionService


def get_submission_service() -> SubmissionService:
    return SubmissionService()
