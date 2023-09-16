from typing import Generator

from sqlalchemy.ext.declarative import declarative_base
from sqlmodel import Session, create_engine

from .config import get_settings

db_settings = get_settings()
engine = create_engine(db_settings.SQLALCHEMY_DATABASE_URI, echo=True)

Base = declarative_base()


def get_db() -> Generator:
    with Session(engine) as db:

        yield db
