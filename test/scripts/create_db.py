from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from app.config import SQLALCHEMY_DATABASE_URL


def main():
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    session = Session(bind=engine.connect())

    session.execute(text(""" create table image (
    id integer not null primary key,
    request_id varchar(256),
    image_id varchar(256),
    faces json not null 
    );"""))
    session.close()


if __name__ == '__main__':
    main()
