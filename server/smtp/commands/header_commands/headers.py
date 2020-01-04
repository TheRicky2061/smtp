import abc
from server.smtp.constants import reply_codes
from server.smtp.constants import messages
from server.smtp.commands.server_commands.base_command import BaseCommand


class Header(BaseCommand, abc.ABC):

    @abc.abstractmethod
    def apply_header_field(self, header_field):
        pass

    def run(self):

        try:
            header_field = self.message.decode('utf8').split(':')[1].strip()
            self.status_code = reply_codes.ACTION_COMPLETED
            self.response = messages.OK
            self.apply_header_field(header_field)

        except IndexError:
            self.status_code = reply_codes.SYNTAX_ERROR
            self.response = messages.SYNTAX_ERROR

        else:
            self.status_code = reply_codes.ACTION_COMPLETED
            self.response = messages.OK


class Subject(Header):

    def apply_header_field(self, header_field):
        self.email.subject = header_field


class From(Header):

    def apply_header_field(self, header_field):
        self.email.f_rom = header_field


class To(Header):

    def apply_header_field(self, header_field):
        self.email.to = header_field


class Date(Header):

    def apply_header_field(self, header_field):
        self.email.date = header_field
