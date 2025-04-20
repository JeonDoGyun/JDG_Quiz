from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID

from ..schemas.question_schema import QuestionSchema


# 특정 퀴즈 상세 내용 (문제 내용 포함)
class QuizDetailResponse(BaseModel):
    quiz_id: UUID
    title: str
    description: str
    page: int
    total_pages: int
    questions: List[QuestionSchema]


# 퀴즈 목록 단위 형태
class QuizListItemSchema(BaseModel):
    quiz_id: UUID
    title: str
    description: str
    created_by: str
    has_submitted: Optional[bool] = None  # 사용자 전용


# 목록 응답 전체(페이지 포함)
class QuizListResponseSchema(BaseModel):
    quizzes: List[QuizListItemSchema]
    total: int
    page: int
    size: int
