<<<<<<< HEAD
from flask import Flask, request, abort
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    FlexSendMessage, MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

from linebot.models import BubbleContainer

import config
from sales_report import SalesReport

app = Flask(__name__)

line_bot_api = LineBotApi(config.CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(config.CHANNEL_SECRET)

# Template format definition
# Plus, the template was made on the LINE Flex Message Simulator
template_env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml', 'json'])
)

users = []

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    sender_id = event.source.user_id
    if sender_id not in users:
        users.append(sender_id)
    data = SalesReport('REACHED', '#1DB446', '$3000', '$5557');
    template = template_env.get_template('sales-report.json')
    data = template.render(dict(data=data))
    message = FlexSendMessage(alt_text = "Sales Report", contents=BubbleContainer.new_from_json_dict(json.loads(data)))
    line_bot_api.reply_message(event.reply_token, message)
    send_push_message()

def send_push_message():
    data = SalesReport('TO BE REACHED', '#FFC107', '$5557', '$2322');
    template = template_env.get_template('sales-report.json')
    data = template.render(dict(data=data))
    message = FlexSendMessage(alt_text = "Sales Report", contents=BubbleContainer.new_from_json_dict(json.loads(data)))
    for user in users:
        line_bot_api.push_message(user, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
=======





from flask import Flask, request, abort
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    FlexSendMessage, MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

from linebot.models import BubbleContainer
import config
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from sales_report import SalesReport


# creds
scope = ['https://www.googleapis.com/auth/spreadsheets.readonly',
    'https://www.googleapis.com/auth/drive.readonly']
creds = ServiceAccountCredentials.from_json_keyfile_name('dummy.json', scope)
client = gspread.authorize(creds)

date = datetime.datetime.now()

# I had to make a new "integer" variable because I don't know how to code properly, lol 

fMonth = date.strftime("%m")
sMonth = int(fMonth)


# Month loop

if sMonth == 1:
	sheet = client.open("database")._201901

elif sMonth == 2:
	sheet = client.open("database")._201902

elif sMonth == 3:
	sheet = client.open("database")._201903

elif sMonth == 4:
	sheet = client.open("database")._201904

elif sMonth == 5:
	sheet = client.open("database")._201905

elif sMonth == 6:
	sheet = client.open("database")._201906

elif sMonth == 7:
	sheet = client.open("database")._201907

elif sMonth == 8:
	sheet = client.open("database")._201908

elif sMonth == 9:
	sheet = client.open("database")._201909

elif sMonth == 10:
	sheet = client.open("database")._2019010

elif sMonth == 11:
	sheet = client.open("database")._201911

elif sMonth == 12:
	sheet = client.open("database")._201912



# Day loop

fdate = date.strftime("%d")
sdate = int(fdate)



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


# Token bois

app = Flask(__name__)

line_bot_api = LineBotApi('pDGDz4DzoDyeCQccYHoWMD+h2JUs+myycFqVVrOLV075PVxrGdVV20nMtYqU2BPZryOzofwipzEtPndQifjWSSPrFyy6Jzwv/gWoozGUQDGMJlyVltL0BTaqqfLhjRjlbLxQoKRnEstaw0demRT8VwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9a34a6b435e9799517fe0f238c487760')
line_bot_api = LineBotApi(config.CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(config.CHANNEL_SECRET)



# bot boi

def bot():

	# I don't even know why I am declaring global all of these lmao
	# I wrote an "O" after the variable name to indicate these are output variables

	global month
	global current
	global left
	global monthlyObj
	global objList
	global pastList
	global currentDate

	global objectivestatus_o 	
	global date_o 

	global lastYearSales_o
	global objective_o 
	global totalSales_o 

	global threepm_o 
	global sixpm_o 
	global ninepm_o 

	global changetxt_o 
	global change_o 

	global monthlyObj_o 
	global current_o 

	global left_o 
	global percentage_o 
	
	while True:

		# MConverting all of the values into integers
		
		monthlyObj = int(monthObjList)

		lastYearSales = int(pastList)
		objective = int(objList)
		
		# So this is supposed to be user input, the only texts the user will send throught the day
		# This part is a dummy btw
		
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
			changetxt = "Increase "
			
		elif change < 1.00:
			changetxt = "Decrease "
			
		else:
			changetxt = " error"

		
		# Whether the objective was reached or not for that day sales

		objectivestatus = ""
		
		if totalSales > objective:
			objectivestatus = "REACHED"
			
		elif totalSales < objective:
			objectivestatus = "NOT REACHED"
			
		else:
			objectivestatus = " error"


			
		# Here we append today's sales to the month dictionary to work with the variables below

		month.append(totalSales)
		current = sum(month)
		left = int(monthlyObj) - int(current)
		percentage = int(current / monthlyObj * 100)


		# Class output variables

		objectivestatus_o = str(objectivestatus) 	
		date_o = currentDate.strftime("%Y-%m-%d")

		lastYearSales_o = str("{:,}".format(lastYearSales)) + "円"
		objective_o = str("{:,}".format(objective)) + "円"
		totalSales_o = str("{:,}".format(totalSales)) + "円"

		threepm_o = str("{:,}".format(threepm)) + "円"
		sixpm_o = str("{:,}".format(sixpm)) + "円"
		ninepm_o = str("{:,}".format(ninepm)) + "円"

		changetxt_o = str(changetxt)
		change_o = str(change) + "%"

		monthlyObj_o = str("{:,}".format(monthlyObj)) +  "円"
		current_o = str("{:,}".format(current)) + "円"

		left_o = str("{:,}".format(left)) + "円"
		percentage_o = str(percentage) + "%"











# Template format definition

template_env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml', 'json'])
)

@app.route("/callback", methods=['POST'])
def callback():
    """
    This is the main method that gets called every time someone 
    sends a message to the bot. Here the method handle_message 
    gets invoked. TODO: Messages that
    are not triggered buy the user need another kind of method
    """
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'








# Now now, I have no idea what im doing but please find a way to send scheduled push messages 
# and retrieve the user input to store it as variables threepm, sixpm, ninepm and totalSales













@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    """
    Method to send the response message. TODO: Here, is 
    possible to read the user message to work with wome input
    """
    # Create an object SalesReport to pack the data tha is going
    #  to be sent to the json template
    data = SalesReport(objectivestatus_o, '#1DB446', date_o, lastYearSales_o, totalSales_o, objective_o, threepm_o, sixpm_o, ninepm_o, change_o, monthlyObj_o, current_o, left_o, percentage_o);
    template = template_env.get_template('sales-report.json')
    data = template.render(dict(data=data))
    # Send the structured message. Note, the template needs to be parsed to 
    # an Flex MessageUI element, in this case a BubbleContainer
    message = FlexSendMessage(alt_text = "Alt Text", contents=BubbleContainer.new_from_json_dict(json.loads(data)))
    line_bot_api.reply_message(event.reply_token, message)

import os

# Initial method to be run by the server
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    port = int(config.PORT)
    app.run(host='0.0.0.0', port=port) 
>>>>>>> be26ed06a2822dae9e766860786d92139376222a
