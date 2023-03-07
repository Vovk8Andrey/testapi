from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

from app.config import SQLALCHEMY_DATABASE_URL


Base = declarative_base()


def connect_db():
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={})
    session = Session(bind=engine.connect())
    return session


class Image(Base):
    __tablename__ = 'image'

    id = Column(Integer, primary_key=True, nullable=False)
    request_id = Column(String(255), nullable=False)
    image_id = Column(String(255), nullable=False)
    faces = Column(JSON)


