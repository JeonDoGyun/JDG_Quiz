from uuid import UUID
from fastapi import APIRouter, Depends, Query

from ..controllers.quiz_dependency import get_current_user_id, get_current_user_role, get_quiz_read_service
from ..schemas.quiz_schema import QuizDetailResponse, QuizListResponseSchema
from ..services.quiz_read_service import QuizReadService

from django_app.user.permissions.roles import Role


router = APIRouter(prefix="/quizzes", tags=["Quizzes"])


@router.get("", response_model=QuizListResponseSchema)
def get_quiz_list(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),  # default는 예시처럼 10으로 설정
    user_id: str = Depends(get_current_user_id),
    role: Role = Depends(get_current_user_role),
    quiz_service: QuizReadService = Depends(get_quiz_read_service)
):
    return quiz_service.get_quiz_list(role=role, user_id=user_id, page=page, size=size)


@router.get("/{quiz_id}", response_model=QuizDetailResponse)
def get_quiz_detail(
    quiz_id: UUID,
    page: int = Query(1, ge=1),
    quiz_service: QuizReadService = Depends(get_quiz_read_service)
):
    return quiz_service.get_quiz_detail(quiz_id=quiz_id, page=page)
