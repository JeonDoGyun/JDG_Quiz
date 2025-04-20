from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class SubmittedAnswer(BaseModel):
    question_id: int
    selected_choice_id: str  # 사용자가 고른 선택지


class AnswerSubmissionRequest(BaseModel):
    answers: List[SubmittedAnswer]


class SubmissionResultResponse(BaseModel):
    submission_id: str
    score: Optional[int]
    submitted_at: Optional[datetime]
    message: str
