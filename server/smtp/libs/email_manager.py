import threading
import socket

from server.smtp.destination_mail_server import DestinationMailServer
from server.smtp.inbox import Inbox


class EmailManager(threading.Thread):

    def __init__(self, emails, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.emails = emails
        self.inbox = Inbox()

    def run(self):

        while True:

            email = self.emails.get()

            print(email)

            if email is None:
                break

            if email.destination_host == self.ip:
                # Save to inbox if this is the destination
                print("Message saved to inbox")
                self.inbox.save(email)

            else:
                # Send to Destination Mail Server
                mail_server = DestinationMailServer(host=email.destination_host, port=email.destination_port)

                try:
                    mail_server.send(email)

                except ConnectionRefusedError as error:
                    print(error)

    @property
    def ip(self):
        return socket.gethostbyname(socket.gethostname())
