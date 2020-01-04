import abc


class BaseCommand:

    def __init__(self, request=None, user='', message='', email=None):
        self.request = request
        self.user = user
        self.message = message
        self.email = email
        self.status_code = 0
        self.response = ''

    def execute(self):
        self.run()
        response = self.get_response()
        print("Sending", response)
        self.request.sendall(response)

    def run(self):
        raise NotImplementedError

    def get_response(self):
        return f'{self.status_code} {self.response}\n'.encode('utf-8')

