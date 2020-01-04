from server.smtp.commands.server_commands.data import Data
from server.smtp.commands.server_commands.helo import Helo
from server.smtp.commands.server_commands.mail_from import MailFrom
from server.smtp.commands.server_commands.quit import Quit
from server.smtp.commands.server_commands.rcpt_to import RcptTo
from server.smtp.commands.server_commands.unrecognized import Unrecognized
from server.smtp.constants import commands


class CommandSelector:

    def __init__(self, message=b''):
        self.message = message
        self.command = self.select(message)

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, new_message):
        self.__message = new_message.decode('utf8')
        self.command = self.select(new_message)

    @staticmethod
    def select(message):

        command = Unrecognized

        if message.lower().startswith(commands.HELO):
            command = Helo

        elif message.lower().startswith(commands.MAIL_FROM):
            command = MailFrom

        elif message.lower().startswith(commands.RCPT_TO):
            command = RcptTo

        elif message.lower().startswith(commands.DATA):
            command = Data

        elif message.lower().startswith(commands.QUIT):
            command = Quit

        return command
