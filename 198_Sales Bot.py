



month = []
monthlyObj = int(input("Monthly Objective: "))

def bot():
	
	global month
	global current
	global left
	global monthlyObj
	
	
	while True:
		
		lastYearSales = int(input("Last Year Sales: ")) 
		objective = int(input("Objective: "))
		
		
		threepm = int(input("3 PM: "))
		sixpm = int(input("6 PM: "))
		ninepm = int(input("9 PM: "))
		
		totalSales = int(threepm + sixpm + ninepm)
		change = int(totalSales/lastYearSales*100-100)
		changetxt = ""
		
		
		
		
		if change > 1:
			changetxt = " increase"
			
		elif change < 1:
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
			
		print("Last Year Sales: "+ str(lastYearSales) + "円")
		print("Objective: " + str(objective) + "円" + "\n\n")
		print("3 PM: " + str(threepm) + "円")
		print("6 PM: " + str(sixpm) + "円")
		print("9 PM: " + str(ninepm) + "円" + "\n\n")
		print("Sales: " + str(totalSales) + "円" + "\n\n")
		print(str(change) + "%" + str(changetxt) + " from last year.")
		print("Objective" + str(objectivestatus) + "\n")
		
		print("Monthly Objective: " + str(monthlyObj) +  "円")
		
		print("Current Monthly Sales: " + str(current) + "円" + "\n")
		print("Amount left to reach objective: " + str(left) + "円")
		print("Progress: " + str(percentage) + "%" + "\n\n")
		print("______________________________________" + "\n\n")
		
	
		
	
		
bot()
	

		
	







