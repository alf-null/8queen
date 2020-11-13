"""
Database configuration file
"""

import urllib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


db_driver = "postgres+psycopg2"
user = "postgres"
password = "example"
host = "db"
port = "5432"
database = "postgres"

DATABASE_URI = f"{db_driver}://{user}:{password}@{host}:{port}/{database}"
Base = declarative_base()

engine = create_engine(DATABASE_URI)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
session = Session(bind=engine)
