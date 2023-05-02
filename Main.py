from icalendar import Calendar
import FileSys
import DataBaseSys


def display(cal):
    return cal.to_ical().decode("utf-8").replace('\r\n', '\n').strip()


FileSys.create_file()
file = open('example.ics', 'rb')
cal_file = Calendar.from_ical(file.read())
for component in cal_file.walk():
    if component.name == "VEVENT":
        attendee = component.get("attendee")
        organiser = component.get("organizer")
        summary = component.get("summary")
        start = component.decoded("dtstart")
        end = component.decoded("dtend")
list = DataBaseSys.get_users()
for i in range(len(list)):
    if attendee[7:] == list[i][1]:
        DataBaseSys.add_event(attendee[7:], start, end, summary)
    if organiser[7:] == list[i][1]:
        DataBaseSys.add_event(organiser[7:], start, end, summary)

file.close()
