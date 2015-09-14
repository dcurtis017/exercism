from datetime import datetime
#import time
from datetime import timedelta
def add_gigasecond(dt):
	#return datetime.fromtimestamp(time.mktime(dt.timetuple())+10**9)
	#the above is 1 hour off, not sure why
	return dt+timedelta(seconds=10**9)