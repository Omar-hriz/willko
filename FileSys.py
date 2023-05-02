from icalendar import Calendar, Event, vCalAddress,vText
from datetime import datetime
import pytz

organizer = vCalAddress('MAILTO:noone@example.com')
organizer.params['cn'] = vText('Willko')
organizer.params['role'] = vText('CEO')
attendee = vCalAddress('MAILTO:maxm@example.com')
attendee.params['cn'] = vText('Willko')
attendee.params['ROLE'] = vText('REQ-PARTICIPANT')


def generate():
    cal = Calendar()
    event = Event()
    event.add('summary', 'Test Event')
    event.add('dtstart', datetime(2023, 5, 2, 8, 0, 0, tzinfo=pytz.timezone("Europe/Paris")))
    event.add('dtend', datetime(2023, 5, 2, 10, 0, 0, tzinfo=pytz.timezone("Europe/Paris")))
    event.add("organizer", organizer)
    event.add("attendee", attendee)
    cal.add("PRODID", '-//Microsoft Corporation//Outlook<SP>')
    cal.add("VERSION", "1.0")
    cal.add_component(event)
    return cal


def create_file():
    f = open('example.ics', 'wb')
    f.write(generate().to_ical())
    f.close()
