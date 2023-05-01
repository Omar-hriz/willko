from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone


def display(cal):
    return cal.to_ical().decode("utf-8").replace('\r\n', '\n').strip()