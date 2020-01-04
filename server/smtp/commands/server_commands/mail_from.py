from .address import Address


class MailFrom(Address):

    def __init__(self, *args, **kwargs):
        super().__init__('mail_from', *args, **kwargs)
