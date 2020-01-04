from server import Database
from server import Email
from server import User

if __name__ == '__main__':

    username = 'enrique.rodriguez9'

    db = Database()

    user = User(username=username)

    db.store(user)

    email = Email(user=user, source_address='email@server.com', source_username='The Don', subject='email', message='message')

    db.store(email)

    user = db.fetch_user(username)

    emails = db.fetch_emails_by_user(username)

    print(emails[0])


