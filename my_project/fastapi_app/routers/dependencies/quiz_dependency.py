from ...services.quiz_read_service import QuizReadService

from django_app.user.permissions.roles import Role


def get_quiz_read_service() -> QuizReadService:
    return QuizReadService()


def get_current_user_id() -> str:
    return "testing-user-id"


def get_current_user_role() -> Role:
    return Role.USER
