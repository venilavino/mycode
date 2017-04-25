import datetime

weekno = datetime.datetime.today().weekday()

if weekno<5:
    print "Weekday"
else:
    print "Weekend"
