from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import relationship

from ..db.base import Base


class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(
        Integer,
        ForeignKey("courses.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=True)
    video = Column(String(500), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    course = relationship(
        "Course",
        back_populates="lessons",
    )

    exercises = relationship(
        "Exercise",
        back_populates="lesson",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return (
            f"<Lesson(id={self.id}, title='{self.title}', course_id={self.course_id})>"
        )
