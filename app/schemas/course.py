from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class CourseBase(BaseModel):
    author_id: int = Field(description="ID of the author of course", gt=0)

    title: str = Field(
        min_length=3,
        max_length=200,
        description="Course title",
        examples=["Python for beginners"],
    )
    description: Optional[str] = Field(
        None,
        description="Course description",
        examples=["Complete Python course from basics"],
    )


class CourseCreate(CourseBase):
    pass


class CourseUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=200)

    description: Optional[str] = None


class CourseResponse(CourseBase):
    id: int = Field(description="Unique id")
    created_at: datetime = Field(description="Creation date")
    updated_at: datetime = Field(description="Modification date")

    model_config = {"from_attributes": True}
