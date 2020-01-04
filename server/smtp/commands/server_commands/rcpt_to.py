from .address import Address


class RcptTo(Address):

    def __init__(self, *args, **kwargs):
        super().__init__('rcpt_to', *args, **kwargs)
