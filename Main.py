from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone
import GenerateFile


def display(cal):
    return cal.to_ical().decode("utf-8").replace('\r\n', '\n').strip()


print(display(GenerateFile.generate()))
