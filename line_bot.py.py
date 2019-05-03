

import numpy as np
import nltk 
import random 
import string
import pprint
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://www.googleapis.com/auth/spreadsheets.readonly',
    'https://www.googleapis.com/auth/drive.readonly']
creds = ServiceAccountCredentials.from_json_keyfile_name('dummy.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("201905").sheet1

# Extract and print all of the values
objList = sheet.acell('G5').value
pastList = sheet.acell('H5').value

objList = objList.replace(',','')
pastList = pastList.replace(',','')


month = []
monthlyObj = int(input("Monthly Objective: "))




def bot():
	
	global month
	global current
	global left
	global monthlyObj
	global objList
	global pastList
	
	while True:
		
		lastYearSales = int(pastList)
		objective = int(objList)
		
		
		threepm = int(input("3 PM: "))
		sixpm = int(input("6 PM: "))
		ninepm = int(input("9 PM: "))
		dailytotal = int(input("Daily Total: "))
		
		totalSales = dailytotal
		change = int(totalSales/lastYearSales*100-100)
		changetxt = ""
		
		
		
		
		if change > 1.00:
			changetxt = " increase"
			
		elif change < 1.00:
			changetxt = " decrease"
			
		else:
			changetxt = " error"
		
		objectivestatus = ""
		
		if totalSales > objective:
			objectivestatus = " reached ✅"
			
		elif totalSales < objective:
			objectivestatus = " not reached ❌"
			
		else:
			objectivestatus = " error"
			
		month.append(totalSales)
		current = sum(month)
		left = int(monthlyObj - current)
		percentage = int(current/monthlyObj*100)
			
			
		print("\n\n")
		print("______________________________________" + "\n\n")
			
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
	

		
	



