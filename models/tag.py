from models import Base, with_row_locks
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
)
from utils.db_session import provide_db_session


class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, ForeignKey('tag.id'), primary_key=True)
    tag = Column(String(255), primary_key=True)

    def __init__(self, qn_id, tag):
        self.id = qn_id
        self.tag = tag

    def __repr__(self):
        return '<Tag id={} tag={}>'.format(self.id,
                                                                self.tag)

    @staticmethod
    @provide_db_session
    def get(id,db=None):
        tag = with_row_locks(db.session.query(Tag).filter(
            Tag.id == id, of=Tag)).first()
        return tag


    @staticmethod
    @provide_db_session
    def delete(id,db=None):
        with_row_locks(db.session.query(Tag).filter(
            Tag.id == id), of=Tag).delete()
