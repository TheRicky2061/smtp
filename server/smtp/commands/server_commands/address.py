from server.smtp.constants import reply_codes
from server.smtp.constants import messages
from server.smtp.libs.email_verifier import EmailVerifier
from server.smtp.exceptions import BadSequenceError, InvalidAddress
from .base_command import BaseCommand


class Address(BaseCommand):

    def __init__(self, address_type=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email_verifier = EmailVerifier()
        self.address_type = address_type

    def run(self):

        email_address = None

        try:
            if self.user.name is None:
                raise BadSequenceError

            email_address = self.message.decode('utf8').split(':', maxsplit=1)[1].strip()

            if not self.email_verifier.is_valid_email(email_address):
                raise InvalidAddress

            self.status_code = reply_codes.ACTION_COMPLETED
            self.response = messages.SENDER_OK.format(email_address)
            self.set_address_to_email()

        except IndexError:
            self.status_code = reply_codes.SYNTAX_ERROR
            self.response = messages.SYNTAX_ERROR

        except BadSequenceError:
            self.status_code = reply_codes.BAD_SEQUENCE
            self.response = messages.HELO_FIRST

        except InvalidAddress:
            self.status_code = reply_codes.INVALID_ADDRESS
            self.response = messages.INVALID_ADDRESS.format(email_address)

    def set_address_to_email(self):

        if self.address_type == 'mail_from':
            self.email.mail_from = self.email_verifier.email
        elif self.address_type == 'rcpt_to':
            self.email.rcpt_to = self.email_verifier.email
        else:
            raise ValueError("Invalid address type")
