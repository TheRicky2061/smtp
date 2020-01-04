from server.smtp.constants import reply_codes
from server.smtp.constants import messages
from .base_command import BaseCommand


class Quit(BaseCommand):

    def run(self):
        self.status_code = reply_codes.SERVER_CLOSING
        self.response = messages.SERVER_CLOSING
