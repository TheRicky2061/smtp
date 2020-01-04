from server.smtp.constants import reply_codes
from server.smtp.constants import messages
from .base_command import BaseCommand


class Helo(BaseCommand):

    def run(self):

        try:
            self.user.name = self.message.split()[1].decode('utf8')
            self.status_code = reply_codes.ACTION_COMPLETED
            self.response = messages.HELO_MESSAGE.format(self.user.name)

        except IndexError:
            self.status_code = reply_codes.SYNTAX_ERROR
            self.response = messages.SYNTAX_ERROR
