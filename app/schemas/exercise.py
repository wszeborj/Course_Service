from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class ExerciseBase(BaseModel):
    title: str = Field(
        min_length=3,
        max_length=200,
        examples=["Write sum function"]
    )
    content: Optional[str] = Field(
        None,
        description="Description of exercise"
    )
    exercise: Optional[str] = Field(
        None,
        description="Specific exercise to complete"
    )


class ExerciseCreate(ExerciseBase):
    lesson_id: int = Field(
        description="ID of the lesson to which the exercise belongs",
        gt=0
    )

class ExerciseUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=200)
    content: Optional[str] = None
    exercise: Optional[str] = None


class ExerciseResponse(ExerciseBase):
    id: int
    lesson_id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}