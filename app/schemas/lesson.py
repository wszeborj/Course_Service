from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class LessonBase(BaseModel):
    title: str = Field(
        ...,
        min_length=3,
        max_length=200,
        examples=["Introduction to variables"]
    )
    content: Optional[str] = Field(
        None,
        description="Text content of the lesson"
    )
    video: Optional[str] = Field(
        None,
        max_length=500,
        description="URL to wideo (YouTube, Vimeo, itp.)",
        examples=["https://youtube.com/watch?v=xxx"]
    )


class LessonCreate(LessonBase):
    course_id: int = Field(
        description="ID of the course to which the lesson belongs",
        gt=0
    )

class LessonUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=200)
    content: Optional[str] = None
    video: Optional[str] = Field(None, max_length=500)
    exercise: Optional[str] = None

class LessonResponse(LessonBase):

    id: int
    course_id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}