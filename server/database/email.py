from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from server.database.base import Base


class Email(Base):
    __tablename__ = 'emails'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    source_address = Column(String)
    source_username = Column(String)
    subject = Column(String)
    message = Column(String)

    user = relationship('User', back_populates='emails')

    def __str__(self):
        string = '----------------------------\n'
        string += f'From: {self.source_username} <{self.source_address}>\n'
        string += f'Subject: {self.subject}\n'
        string += f'\n{self.message}\n'
        string += '----------------------------'

        return string
