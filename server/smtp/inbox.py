from server.database import Database
from server.database.email import Email


class Inbox:

    def __init__(self):
        self.db = Database()

    def save(self, email):
        user = self.db.fetch_user(email.source_username)

        db_email = Email(user=user, source_username=email.mail_from, subject=email.subject, message=email.data)

        self.db.store(db_email)

