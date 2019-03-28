import unittest
from user import User
from event import Event
from event_request_bot import create_request

class EventRequestTests():
    def __init__(self):
        self.user = None
        self.event = None

    def set_up(self):
        self.user = User('', 'amr439', '1234567890', 'FISDU', '123456')
        self.event = Event('Test Event', 'Test description', '01 Apr 2019', '01:15 PM', '02:15 PM',
                           'Drexel Park', '200', '$20')

    def test_create(self):
        self.set_up()
        create_request(self.user, self.event)


if __name__ == '__main__':
    test = EventRequestTests()
    test.test_create()
