from models import Base, with_row_locks
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Text,
    DateTime,
)
from datetime import datetime


class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True, autoincrement=True)
    qn_id = Column(Integer, ForeignKey("question.id"), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    content = Column(Text, nullable=False)
    likes = Column(Integer, nullable=False, default=0)
    dislikes = Column(Integer, nullable=False, default=0)

    def __init__(self, qn_id, content, created_at=datetime.now(), likes=0, dislikes=0):
        self.qn_id = qn_id
        self.content = content
        self.created_at = created_at
        self.likes = likes
        self.dislikes = dislikes
