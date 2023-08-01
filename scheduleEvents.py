"""
Usage: python3 scheduleEvents.py
Output: ics file
"""
def main():
    startDate = '20230806' # INPUT: recording start date (YYYYMMDD)
    endDate   = '1'        # INPUT: number of days to schedule
    name      = 'record'   # INPUT: name of event

    # Schedule 1 minute event every 10 minutes
    events = open(f'{name}.ics', 'w')
    events.write('BEGIN:VCALENDAR\n')
    for hour in range(0, 24):
        for minute in range(0, 60, 10):
            events.write('BEGIN:VEVENT\n')
            events.write(f'DTSTART;TZID=America/Los_Angeles:{startDate}T{hour:02d}{minute:02d}00\n')
            events.write(f'DTEND;TZID=America/Los_Angeles:{startDate}T{hour:02d}{minute+1:02d}00\n')
            events.write(f'RRULE:FREQ=DAILY;COUNT={endDate}\n')
            events.write(f'SUMMARY:{name}\n')
            events.write('END:VEVENT\n')
    events.write("END:VCALENDAR")
    events.close()

if __name__ == "__main__":
    main()
