

class Email:

    def __init__(self, mail_from='', f_rom='', rcpt_to='', to='', subject='', data='', date=''):
        self.mail_from = mail_from
        self.f_rom = f_rom
        self.to = to
        self.rcpt_to = rcpt_to
        self.subject = subject
        self.date = date
        self.data = data

    @property
    def source_username(self):
        return self.mail_from.split('@')[0]

    @property
    def destination_host(self):
        return self.rcpt_to.split('@')[1].split(':')[0]

    @property
    def destination_port(self):
        return int(self.rcpt_to.split('@')[1].split(':')[1])

    def __str__(self):
        string = '----------------------------\n'
        string += f'From: {self.f_rom} <{self.mail_from}>\n'
        string += f'To: {self.to} <{self.rcpt_to}>\n'
        string += f'Subject: {self.subject}\n'
        string += f'\n{self.data}\n'
        string += '----------------------------'

        return string
