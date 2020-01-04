import socket
import socketserver
import sys
from queue import Queue

from server import MailServer
from server.smtp.libs.email_manager import EmailManager

HOST, PORT = '', 25


if __name__ == '__main__':
    try:
        PORT = int(sys.argv[1])

    except Exception as e:
        pass

    with socketserver.TCPServer((HOST, PORT), MailServer) as server:
        address = socket.gethostbyname(socket.gethostname())

        print(f"Mail server running on {address}:{PORT}")

        emails = Queue()

        email_manager = EmailManager(emails)

        server.queue = emails

        try:
            email_manager.start()
            server.serve_forever()

        except Exception as e:
            print(e)
            server.server_close()
            emails.put(None)
            email_manager.join()
