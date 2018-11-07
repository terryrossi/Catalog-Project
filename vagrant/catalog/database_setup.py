import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Category(Base):
    """docstring fs Category."""
    __tablename__ = 'category'

    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)

class Product(Base):
    """docstring fs Product."""
    __tablename__ = 'product'

    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    description = Column(String(250))
    price = Column(String(8))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)


########## insert at end of file ##############

engine = create_engine('sqlite:///Amazon.db')
Base.metadata.create_all(engine)
