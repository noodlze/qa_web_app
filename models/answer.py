from models import Base, with_row_locks
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Text,
    DateTime,
)
from datetime import datetime
from utils.db_session import provide_db_session


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

    def __repr__(self):
        return '<Answer qn_id={} content={} created_at={} likes={} dislikes={}>'.format(self.qn_id,
                                                                            self.content,
                                                                            self.created_at,
                                                                            self.likes,
                                                                            self.dislikes)

    @staticmethod
    @provide_db_session
    def get(id,db=None):
        answer = with_row_locks(db.session.query(Answer).filter(
            Answer.id == id, of=Answer)).first()
        return answer


    @staticmethod
    @provide_db_session
    def delete(id,db=None):
        with_row_locks(db.session.query(Answer).filter(
            Answer.id == id), of=Answer).delete()
