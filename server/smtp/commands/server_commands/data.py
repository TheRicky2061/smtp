from server.smtp.constants import reply_codes
from server.smtp.constants import messages
from server.smtp.commands.header_commands.headers import From, To, Subject, Date
from .base_command import BaseCommand

FROM = b'from:'
TO = b'to:'
SUBJECT = b'subject:'
DATE = b'date:'


class Data(BaseCommand):

    def run(self):

        if self.user is None:
            self.status_code = reply_codes.BAD_SEQUENCE
            self.response = messages.HELO_FIRST
            return

        if self.email.mail_from == '':
            self.status_code = reply_codes.BAD_SEQUENCE
            self.response = messages.BAD_SEQUENCE
            return

        if self.email.rcpt_to == '':
            self.status_code = reply_codes.BAD_SEQUENCE
            self.response = messages.RCPT_FIRST
            return

        self.status_code = reply_codes.START_MESSAGE
        self.response = messages.START_MESSAGE
        self.retrieve_message()

    def retrieve_message(self):

        response = self.get_response()
        self.request.sendall(response)


        while True:

            self.message = self.request.recv(4096)

            print('message:', self.message)

            if messages.CRLF in self.message:
                self.email.data += self.message.strip(messages.CRLF).decode('utf8')
                break

            command = None

            if self.message.lower().startswith(FROM):
                command = From

            elif self.message.lower().startswith(TO):
                command = To

            elif self.message.lower().startswith(SUBJECT):
                command = Subject

            elif self.message.lower().startswith(DATE):
                command = Date

            print('command:', command)

            if command is None:
                self.email.data += self.message.decode('utf8')
                self.request.sendall(b' ')

            else:
                command(request=self.request, message=self.message, email=self.email).execute()

        self.status_code = reply_codes.ACTION_COMPLETED
        self.response = messages.OK
