from models import Base, with_row_locks
from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
)
from datetime import datetime
from utils.db_session import provide_db_session

class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    content = Column(Text, nullable=False)
    likes = Column(Integer, nullable=False, default=0)
    dislikes = Column(Integer, nullable=False, default=0)

    def __init__(self, content, created_at=datetime.now(), likes=0, dislikes=0):
        self.content = content
        self.created_at = created_at
        self.likes = likes
        self.dislikes = dislikes

    def __repr__(self):
        return '<Question content={} created_at={} likes={} dislikes={}>'.format(self.content,
                                                                                self.created_at,
                                                                                self.likes,
                                                                                self.dislikes)

    @staticmethod
    @provide_db_session
    def get(id,db=None):
        question = with_row_locks(db.session.query(Question).filter(
            Question.id == id, of=Question)).first()
        return question


    @staticmethod
    @provide_db_session
    def delete(id,db=None):
        with_row_locks(db.session.query(Question).filter(
            Question.id == id), of=Question).delete()
