
import datetime
import time
import schedule

date = datetime.datetime.now()
timeStr = date.strftime("%H:%M")


def first():
	print("First input ")

def second():
	print("Second Input ")

def third():
	print("Third Input ")

def final():
	print("Final Input ")



schedule.every().day.at("19:22").do(first)
schedule.every().day.at("19:23").do(second)
schedule.every().day.at("19:24").do(third)
schedule.every().day.at("19:25").do(final)


while True:
    schedule.run_pending()
    time.sleep(1)
