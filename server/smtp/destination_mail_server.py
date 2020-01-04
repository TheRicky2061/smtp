import socket

from server.smtp.libs.email import Email


class DestinationMailServer:

    def __init__(self, host, port=25):
        address = socket.gethostbyname(socket.gethostname())
        self.hostname = 'smpt@{address}'.format(address=address)
        self.host = host
        self.port = port

        self.socket = None
        self.email = None
        self.reply_code = None
        self.message = None

    def connect_to_server(self):
        print("From dest")
        print(self.host, self.port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def send(self, email):

        self.email = email

        self.helo()
        self.mail_from()
        self.rcpt_to()
        self.data()
        self.quit()

    def helo(self):
        self.connect_to_server()
        self.send_command(f'helo {self.hostname}\r\n')

    def mail_from(self):
        self.send_command(f'mail from: <{self.email.mail_from}>\r\n')

    def rcpt_to(self):
        self.send_command(f'rcpt to: <{self.email.rcpt_to}>\r\n')

    def data(self):

        self.send_command('data\r\n')

        self.send_mail_from(self.email.f_rom)
        self.send_mail_to(self.email.to)
        self.send_subject(self.email.subject)
        self.send_date(self.email.date)

        self.send_command(self.email.data + '.\r\n')

    def send_mail_from(self, mail_from):

        if mail_from != '':
            self.send_command(f'from: {mail_from}\r\n')

    def send_mail_to(self, mail_to):

        if mail_to != '':
            self.send_command(f'to: {mail_to}\r\n')

    def send_subject(self, subject):

        if subject != '':
            self.send_command(f'subject: {subject}\r\n')

    def send_date(self, date):

        if date != '':
            self.send_command(f'date: {date}\r\n')

    def quit(self):
        self.send_command('quit\r\n')
        self.close_connection()

    def send_command(self, command, reply_expected=True):
        self.socket.sendall(command.encode('utf8'))

        if reply_expected:
            self.reply_code, self.message = self.get_response()

    def get_response(self):
        response = self.socket.recv(4096)
        reply_code, message = response.decode('utf8').split(' ', maxsplit=1)
        print(reply_code, message)

        return int(reply_code), message

    def close_connection(self):
        self.socket.close()
        self.socket = None


if __name__ == '__main__':
    mail_server = DestinationMailServer(host='localhost')

    the_email = Email(mail_from='enrique@192.168.43.163:25', rcpt_to='other@localhost:4000', f_rom='Person', to='Other', subject='The Email', data='This\r\nIs\r\nThe\r\nEmail')

    mail_server.send(the_email)
