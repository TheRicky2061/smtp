import socketserver

from server.smtp.command_selector import CommandSelector
from server.smtp.libs.email import Email
from server.smtp.commands.server_commands.data import Data
from server.smtp.commands.server_commands.quit import Quit
from server.smtp.user import User


BUFFER_SIZE = 4096


class MailServer(socketserver.BaseRequestHandler):
    allow_reuse_address = True

    def handle(self):

        user = User()
        current_email = Email()
        command_selector = CommandSelector()

        while command_selector.command != Quit:

            message = self.request.recv(BUFFER_SIZE)

            command_selector.message = message

            command_selector.command(self.request, user, message, current_email).execute()

            if command_selector.command == Data:
                self.server.queue.put(current_email)
                current_email = Email()
