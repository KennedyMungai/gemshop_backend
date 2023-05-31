"""The db connection file"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SessionLocal = sessionmaker(autocommit=False, autoflush=False)

Base = declarative_base()
