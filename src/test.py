import unittest
from user import User
from event import Event
from event_request_bot import create_request, check_client


class EventRequestTests(unittest.TestCase):
    def setUp(self):
        self.user = User('', 'amr439', '1234567890', 'FISDU', '123456')
        self.event = Event('Test Event', 'Test description', '01 Apr 2019', '01:15 PM', '02:15 PM',
                           'Drexel Park', '200', '$20', False, False, True)

    def test_client(self):
        try:
            check_client()
        except Exception:
            self.fail('check_client() failed. Check to see if the correct GeckoDriver is in use.')

    def test_create(self):
        try:
            create_request(self.user, self.event)
        except Exception:
            self.fail(
                'create_request() failed. Check client to see where it got stuck, or run test again if something '
                'unexpect happened.')


if __name__ == '__main__':
    unittest.main()
