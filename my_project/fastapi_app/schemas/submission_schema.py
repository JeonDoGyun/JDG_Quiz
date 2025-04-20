from uuid import UUID
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


class ChoiceSnapshot(BaseModel):
    choice_id: str
    text: str


class QuestionSnapshot(BaseModel):
    question_id: int
    description: str
    choices: List[ChoiceSnapshot]


# swagger docs 형태를 위해 따로 만들어주었음
class SubmissionInitResponse(BaseModel):
    submission_id: UUID
    quiz_id: UUID
    questions: List[QuestionSnapshot]
