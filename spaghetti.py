
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# creds
scope = ['https://www.googleapis.com/auth/spreadsheets.readonly',
    'https://www.googleapis.com/auth/drive.readonly']
creds = ServiceAccountCredentials.from_json_keyfile_name('dummy.json', scope)
client = gspread.authorize(creds)


date = datetime.datetime.now()

# I had to make a new "integer" variable because I don't know how to code properly, lol 

fMonth = date.strftime("%m")
sMonth = int(fMonth)

# Now hear me out, as ugly as this looks it actuaLly works using if statements for the sheet coordinates and values as well as the current date

# First starting out with opening the correct spreadsheet depending on the month of the year (sheets are made monthly)

if sMonth == 1:
	sheet = client.open("201901").sheet1

elif sMonth == 2:
	sheet = client.open("201902").sheet1

elif sMonth == 3:
	sheet = client.open("201903").sheet1

elif sMonth == 4:
	sheet = client.open("201904").sheet1

elif sMonth == 5:
	sheet = client.open("201905").sheet1

elif sMonth == 6:
	sheet = client.open("201906").sheet1

elif sMonth == 7:
	sheet = client.open("201907").sheet1

elif sMonth == 8:
	sheet = client.open("201908").sheet1

elif sMonth == 9:
	sheet = client.open("201909").sheet1

elif sMonth == 10:
	sheet = client.open("201910").sheet1

elif sMonth == 11:
	sheet = client.open("201911").sheet1

elif sMonth == 12:
	sheet = client.open("201912").sheet1




fdate = date.strftime("%d")
sdate = int(fdate)

# And here doing the same but with the cell values depending on what day of the month it is. 

if sdate == 1:
	objList = sheet.acell('G5').value
	pastList = sheet.acell('H5').value

elif sdate == 2:
	objList = sheet.acell('G6').value
	pastList = sheet.acell('H6').value

elif sdate == 3:
	objList = sheet.acell('G7').value
	pastList = sheet.acell('H7').value

elif sdate == 4:
	objList = sheet.acell('G8').value
	pastList = sheet.acell('H8').value

elif sdate == 5:
	objList = sheet.acell('G9').value
	pastList = sheet.acell('H9').value

elif sdate == 6:
	objList = sheet.acell('G10').value
	pastList = sheet.acell('H10').value

elif sdate == 7:
	objList = sheet.acell('G11').value
	pastList = sheet.acell('H11').value

elif sdate == 8:
	objList = sheet.acell('G12').value
	pastList = sheet.acell('H12').value

elif sdate == 9:
	objList = sheet.acell('G13').value
	pastList = sheet.acell('H13').value

elif sdate == 10:
	objList = sheet.acell('G14').value
	pastList = sheet.acell('H14').value

elif sdate == 11:
	objList = sheet.acell('G15').value
	pastList = sheet.acell('H15').value

elif sdate == 12:
	objList = sheet.acell('G16').value
	pastList = sheet.acell('H16').value

elif sdate == 13:
	objList = sheet.acell('G17').value
	pastList = sheet.acell('H17').value

elif sdate == 14:
	objList = sheet.acell('G18').value
	pastList = sheet.acell('H18').value

elif sdate == 15:
	objList = sheet.acell('G19').value
	pastList = sheet.acell('H19').value

elif sdate == 16:
	objList = sheet.acell('G20').value
	pastList = sheet.acell('H20').value

elif sdate == 17:
	objList = sheet.acell('G21').value
	pastList = sheet.acell('H21').value

elif sdate == 18:
	objList = sheet.acell('G22').value
	pastList = sheet.acell('H22').value

elif sdate == 19:
	objList = sheet.acell('G23').value
	pastList = sheet.acell('H23').value

elif sdate == 20:
	objList = sheet.acell('G24').value
	pastList = sheet.acell('H24').value

elif sdate == 21:
	objList = sheet.acell('G25').value
	pastList = sheet.acell('H25').value

elif sdate == 22:
	objList = sheet.acell('G26').value
	pastList = sheet.acell('H26').value

elif sdate == 23:
	objList = sheet.acell('G27').value
	pastList = sheet.acell('H27').value

elif sdate == 24:
	objList = sheet.acell('G28').value
	pastList = sheet.acell('H28').value

elif sdate == 25:
	objList = sheet.acell('G29').value
	pastList = sheet.acell('H29').value

elif sdate == 26:
	objList = sheet.acell('G30').value
	pastList = sheet.acell('H30').value

elif sdate == 27:
	objList = sheet.acell('G31').value
	pastList = sheet.acell('H31').value

elif sdate == 28:
	objList = sheet.acell('G32').value
	pastList = sheet.acell('H32').value

elif sdate == 29:
	objList = sheet.acell('G33').value
	pastList = sheet.acell('H33').value

elif sdate == 30:
	objList = sheet.acell('G34').value
	pastList = sheet.acell('H34').value

elif sdate == 31:
	objList = sheet.acell('G35').value
	pastList = sheet.acell('H35').value

else:
	print("dateTime error")


# The coordinates for monthObjList will always be the same regardless of current date

monthObjList = sheet.acell('G36').value

# Here we remove the commas from the values for proper integer manipulation

objList = objList.replace(',','')
pastList = pastList.replace(',','')
monthObjList = monthObjList.replace(',','')

# Current date for the output

currentDate = datetime.datetime.now()

# Dictionary that will sum its contents to be showed as results in current, left and percentage

month = []

# Main bot boi

def bot():

	# I don't even know why I am declaring global all of these lmao

	global month
	global current
	global left
	global monthlyObj
	global objList
	global pastList
	global currentDate
	
	while True:

		# MConverting all of the values into integers
		
		monthlyObj = int(monthObjList)

		lastYearSales = int(pastList)
		objective = int(objList)
		
		# So this is supposed to be user input, the only texts the user will send throught the day
		
		threepm = int(input("3 PM: "))
		sixpm = int(input("6 PM: "))
		ninepm = int(input("9 PM: "))
		dailytotal = int(input("Daily Total: "))

		# Some math
		
		totalSales = dailytotal
		change = int(totalSales/lastYearSales*100-100)
		changetxt = ""
		
		
		# Increases or decreases in profit comparing to last year 
		
		if change > 1.00:
			changetxt = " increase"
			
		elif change < 1.00:
			changetxt = " decrease"
			
		else:
			changetxt = " error"

		
		# Whether the objective was reached or not for that day sales

		objectivestatus = ""
		
		if totalSales > objective:
			objectivestatus = " reached ✅"
			
		elif totalSales < objective:
			objectivestatus = " not reached ❌"
			
		else:
			objectivestatus = " error"


			
		# Here we append today's sales to the month dictionary to work with the variables below

		month.append(totalSales)
		current = sum(month)
		left = int(monthlyObj) - int(current)
		percentage = int(current / monthlyObj * 100)
			

		# Annnddd final output	
			
		print("\n\n")
		print("______________________________________" + "\n\n")

		print("[G-Zone銀座ラ・ボエム]  " + currentDate.strftime("%Y-%m-%d") + "\n\n")

		print("Last Year Sales: "+ str("{:,}".format(lastYearSales)) + "円")
		print("Objective: " + str("{:,}".format(objective)) + "円" + "\n\n")
		print("3 PM: " + str("{:,}".format(threepm)) + "円")
		print("6 PM: " + str("{:,}".format(sixpm)) + "円")
		print("9 PM: " + str("{:,}".format(ninepm)) + "円" + "\n\n")
		print("Sales: " + str("{:,}".format(totalSales)) + "円" + "\n\n")
		print(str(change) + "%" + str(changetxt) + " from last year.")
		print("Objective" + str(objectivestatus) + "\n")
		
		print("Monthly Objective: " + str("{:,}".format(monthlyObj)) +  "円")
		
		print("Current Monthly Sales: " + str("{:,}".format(current)) + "円" + "\n")
		print("Amount left to reach objective: " + str("{:,}".format(left)) + "円")
		print("Progress: " + str(percentage) + "%" + "\n\n")
		print("______________________________________" + "\n\n")
		
	
		
	
		
bot()