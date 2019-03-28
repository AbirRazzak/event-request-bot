from event import Event
from user import User
from event_request_bot import create_request


def create_user() -> User:
    user = input('DragonLink username: ')
    number = input('Phone number: ')
    org = input('Org name: ')
    safac = input('SAFAC Account Number: ')
    return User('', user, number, org, safac)


def create_event() -> Event:
    name = input('Name of the event: ')
    desc = input('Event description: ')
    sdate = input('Event start date (XX --- 20XX): ')
    stime = input('Event start time (XX:XX --): ')
    etime = input('Event end time (XX:XX --): ')
    loc = input('Event Location: ')
    estatt = input('Estimated Attendance: ')
    estcost = input('Estimated Cost: ')
    return Event(name, desc, sdate, stime, etime, loc, estatt, estcost)


if __name__ == '__main__':
    print('Hello human, here to make an event?')
    ready = input('Ready? Y/N ')
    if ready == 'y' or ready == 'Y':
        user = create_user()
        event = create_event()
        create_request(user, event)
