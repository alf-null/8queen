"""
Contains schema table/schema to represet the solution boards
"""

from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Solution(Base):
    __tablename__ = "solutions"
    id = Column(Integer, primary_key=True)
    size = Column(Integer)
    board = Column(ARRAY(Integer, dimensions=1))
