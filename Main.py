from icalendar import Calendar
import GenerateFile

def display(cal):
    return cal.to_ical().decode("utf-8").replace('\r\n', '\n').strip()


GenerateFile.create_file()
file = open('example.ics', 'rb')
cal_file = Calendar.from_ical(file.read())
for component in cal_file.walk():
    if component.name == "VEVENT":
        print(component.get("organizer"))
        print(component.get("summary"))
        print(component.decoded("dtstart"))
        print(component.decoded("dtend"))
g.close()