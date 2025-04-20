from uuid import UUID
from pydantic import BaseModel


class ChoiceSchema(BaseModel):
    choice_id: UUID
    text: str
