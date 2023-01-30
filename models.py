from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DATABASE_USER, DATABASE_PASS, DATABASE_HOST, DATABASE_NAME

db_string = f'postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}/{DATABASE_NAME}'

db = create_engine(db_string)
base = declarative_base()


class Schedule(base):
    __tablename__ = 'Schedule'

    id = Column("schedule_weekday_id", Integer, primary_key=True)
    name = Column(String)
    weekday = Column(Integer)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)
