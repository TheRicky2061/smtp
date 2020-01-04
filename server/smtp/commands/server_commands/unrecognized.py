from server.smtp.constants import reply_codes
from server.smtp.constants import messages
from .base_command import BaseCommand


class Unrecognized(BaseCommand):

    def run(self):
        self.status_code = reply_codes.UNRECOGNIZED_COMMAND
        self.response = messages.UNRECOGNIZED_COMMAND
