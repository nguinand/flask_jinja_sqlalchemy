from datetime import datetime
from enum import unique
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql.schema import ForeignKey
from database import Base
import uuid

class Histories(Base):
    __tablename__ = 'histories'
    id = Column(String(50), primary_key=True)
    created_time = Column(DateTime(), nullable=False)
    restaurant_id = Column(String(50), ForeignKey('restaurants.id'))

    def __init__(self, restaurant_id):
        self.id = str(uuid.uuid4())
        self.created_time = datetime.now()
        self.restaurant_id = restaurant_id
    
    def __repr__(self):
        return '<Restaurant %r>' % (self.name)