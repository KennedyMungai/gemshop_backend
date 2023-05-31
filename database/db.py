"""The db connection file"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///gemshop.db',
                       connect_args={'check_same_thread': False}, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False)

Base = declarative_base()


def create_db_and_tables():
    """Creates the database and tables"""
    Base.metadata.create_all(engine)
