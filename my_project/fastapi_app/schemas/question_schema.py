from typing import List
from uuid import UUID
from pydantic import BaseModel

from ..schemas.choice_schema import ChoiceSchema


class QuestionSchema(BaseModel):
    question_id: UUID
    description: str
    choices: List[ChoiceSchema]
