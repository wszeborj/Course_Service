import uuid
from sqlalchemy import Column, String, Text, Boolean, Integer, DateTime, func
from sqlalchemy.orm import relationship
from ..db.base import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, nullable=False)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    lessons = relationship("Lesson",  back_populates="course",  cascade="all, delete-orphan",)


    def __repr__(self):
        return f"<Course(id={self.id}, title='{self.title}')>"