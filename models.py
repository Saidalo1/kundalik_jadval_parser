from sqlalchemy import Column, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DATABASE_USER, DATABASE_PASS, DATABASE_HOST, DATABASE_NAME

db_string = f'postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}/{DATABASE_NAME}'

db = create_engine(db_string)
base = declarative_base()


class Schedule(base):
    __tablename__ = 'Schedule'

    name = Column(String, primary_key=True)
    weekday = Column(String)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)