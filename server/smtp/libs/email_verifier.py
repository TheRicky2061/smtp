import re

'''

'''

class EmailVerifier:
    pattern = '<((.+)@((localhost|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})):(\d{1,4}))>'
    prog = re.compile(pattern)

    def __init__(self):
        self.match = None
        self.email = None
        self.username = None
        self.mail_server = None

    def is_valid_email(self, email):
        self.match = self.prog.match(email)

        if self.match is not None:
            self.email = self.match.group(1)
            self.username = self.match.group(2)
            self.mail_server = self.match.group(3)
            return True

        return False


if __name__ == '__main__':
    verifier = EmailVerifier()

    print(verifier.is_valid_email('<enrique.rodriguez9@123.23.123.123:4000>'))
    print(verifier.email)
    print(verifier.username)
    print(verifier.mail_server)
