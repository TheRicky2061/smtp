from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from server.database.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)

    emails = relationship('Email')
