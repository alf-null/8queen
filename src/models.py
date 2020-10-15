"""
Contains schema table/schema to represet the solution boards
"""

from datetime import datetime
from sqlalchemy import MetaData, Column, Integer, Table
from sqlalchemy.dialects.postgresql import ARRAY

meta = MetaData()
solution_table = Table('solution', meta,
    Column('id', Integer, primary_key=True),
    Column('size', Integer),
    Column('board', ARRAY(Integer, dimensions=2)),
)