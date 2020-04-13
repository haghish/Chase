from datetime import datetime
from datetime import timedelta

# returns the elapsed milliseconds since the start of the program
def millis(startTime):
   dt = datetime.now() - startTime
   ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
   return ms
