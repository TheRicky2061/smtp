from server.database.base import session_factory
from server.database.email import Email
from server.database.user import User


class Database:

    def store(self, orm_object):
        session = session_factory()
        session.add(orm_object)
        session.commit()
        session.close()

    def fetch_user(self, username):
        session = session_factory()

        user = session.query(User).filter(User.username == username).first()

        return user

    def fetch_emails_by_user(self, username):
        user = self.fetch_user(username)

        return user.emails
