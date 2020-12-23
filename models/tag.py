from models import Base, with_row_locks
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
)


class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, ForeignKey('question.id'), primary_key=True)
    tag = Column(String(255), primary_key=True)

    def __init__(self, qn_id, tag):
        self.id = qn_id
        self.tag = tag
