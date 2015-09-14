import calendar
from datetime import date
cal = calendar.Calendar()
def meetup_day(year, month, dow, offset):
	global cal
	days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
	days = list(filter(lambda x: x!= 0 and days[calendar.weekday(year, month, x)] == dow, cal.itermonthdays(year, month)))
	if offset[0].isdigit():
		return date(year, month, days[int(offset[0])-1])
	elif offset == 'last':
		return date(year, month, days[-1])
	else:#teenth
		return date(year, month, list(filter(lambda x: 9 < x < 20, days))[0])
	
	