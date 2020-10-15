"""
Database configuration file
"""

import urllib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import solution_table

db_driver = 'postgres+psycopg2'
user = 'postgres'
password = 'example'
host = 'db'
port = '5432'
database = 'postgres'

DATABASE_URI = f'{db_driver}://{user}:{password}@{host}:{port}/{database}'

engine = create_engine(DATABASE_URI)
db_connection = engine.connect()
solution_insert = solution_table.insert()
