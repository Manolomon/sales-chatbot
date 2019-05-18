from flask import Flask, request, abort
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
import random
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
)

from linebot.models import BubbleContainer

from datetime import datetime, timedelta
import pytz
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import Config
from models.sales_report import SalesReport
from models.sales_update import SalesUpdate
app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(Config.CHANNEL_ACCESS_TOKEN)
# Channel Secret
handler = WebhookHandler(Config.CHANNEL_SECRET)
scope = ['https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('secret-client.json', scope)
client = gspread.authorize(creds)
# Template format definition
# Plus, the template was made on the LINE Flex Message Simulator
template_env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml', 'json'])
)

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
    message = event.message.text
    print(event.source.group_id)
    date = datetime.now(tz=pytz.timezone('Japan'))
    ss = client.open(Config.SPREADSHEET_NAME)
    ws = ss.get_worksheet(date.month - 1)
    content = message.split()
    if content[0] == "/sales":
        print("/sales")
        if len(content) == 2:
            inputt = content[1]
            if inputt.isdigit():
                if date.hour >= 15 and date.hour < 18: # 3 PM
                    ws.update_acell('J' + str(date.day + 4), inputt)
                    response = response_now("3 PM", date)
                elif date.hour >= 18 and date.hour < 21: # 6 PM
                    ws.update_acell('K' + str(date.day + 4), inputt)
                    response = response_now("6 PM", date)
                elif date.hour >= 21 and date.hour < 23:# 9 PM
                    ws.update_acell('L' + str(date.day + 4), inputt)
                    response = response_now("9 PM", date)
                elif date.hour >= 23 and date.minute >= 30: # 11:30 PM Final
                    ws.update_acell('I' + str(date.day + 4), inputt)
                    response = report(date)
                elif date.hour >= 0 and date.hour < 1: # 1 AM Final
                    date = date - timedelta(days=1)
                    ws = ss.get_worksheet(date.month - 1)
                    ws.update_acell('I' + str(date.day + 4), inputt)
                    response = report(date)
                else:
                    response = TextSendMessage(text="Input window currently closed. Try again when a new window opens.")
            else: 
                response = TextSendMessage(text="Sorry, please use only numbers after the command.")
        else:
            response = TextSendMessage(text="Sorry, you are missing the amount parameter")
        line_bot_api.reply_message(event.reply_token, response)
    elif content[0] == "/help":
        print("/help")
        response = "Bot usage: \n/sales <current sales>: To update the database at 3 PM, 6 PM or 9PM. \n/report: To show last sales report.\n/now: To see the status of today's updates.\n/help: To print this message."
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=response))
    elif content[0] == "/report":
        print("/report")
        if date.hour >= 0 and date.hour < 23:
            date = date - timedelta(days=1)
        response = report(date)
        line_bot_api.reply_message(event.reply_token, response)
    elif content[0] == "/now":
        print("/now")
        if date.hour < 15:
            response = TextSendMessage(text="No updates have been made today")
        elif date.hour >= 15 and date.hour < 18:
            response = response_now("3 PM", date)
        elif date.hour >= 18 and date.hour < 21:
            response = response_now("6 PM", date)
        elif date.hour >= 21 and date.hour <= 23:
            response = response_now("9 PM", date)
        line_bot_api.reply_message(event.reply_token, response)
    elif content[0] == "/fail":
        print("/fail")
        msg = TextMessage(text="レポートを忘れたけど店長に言わないでください　(இ﹏இ`｡)")
        line_bot_api.reply_message(event.reply_token, msg)

    elif content[0] == "/asap":
        print("asap")
        msg = TextMessage(text="北村さん、ASAPを付けるのやめてください　ಠ_ಠ　")
        line_bot_api.reply_message(event.reply_token, msg)

    elif content[0] == "/joke":
        print("joke")
        jokeList = ['布団が吹っ飛んだ、、、(ノ͡° ͜ʖ ͡°)ノ︵┻┻', 'あそこのソーダやさんおいしそーだ（´υ｀）', 'もえの家が燃えた(＾艸＾)', 'Covfefe', '北村さん、ASAPを付けるのやめてください　ಠ_ಠ　']
        msg = TextMessage(text=random.choice(jokeList))
        line_bot_api.reply_message(event.reply_token, msg)

def response_now(time ,date):
    ss = client.open(Config.SPREADSHEET_NAME)
    ws = ss.get_worksheet(date.month - 1)
    threepm = ws.acell('J' + str(date.day + 4)).value
    sixpm = ws.acell('K' + str(date.day + 4)).value
    ninepm = ws.acell('L' + str(date.day + 4)).value
    if not (threepm or sixpm or ninepm):
        return TextSendMessage(text="No updates have been made today")
    if threepm:
        threepm = int(threepm)
        threepm = str("{:,}".format(threepm)) + "円"
        current = threepm
    else: 
        threepm = 'TBA'
    if sixpm:
        sixpm = int(sixpm)
        sixpm = str("{:,}".format(sixpm)) + "円"
        current = sixpm
    else: 
        sixpm = 'TBA'
    if ninepm:
        ninepm = int(ninepm)
        ninepm = str("{:,}".format(ninepm)) + "円"
        current = ninepm
    else: 
        ninepm = 'TBA'
    objList = ws.acell('G' + str(date.day + 4)).value
    pastList = ws.acell('H' + str(date.day + 4)).value
    objList = objList.replace(',','')
    pastList = pastList.replace(',','')
    objList = int(objList)
    pastList = int(pastList)

    lastYearSales = int(pastList)
    objective = int(objList)

    date_o = date.strftime("%A, %B %d %Y")
    lastYearSales_o = str("{:,}".format(lastYearSales)) + "円"
    objective_o = str("{:,}".format(objective)) + "円"

    report = SalesUpdate(time, date_o, lastYearSales_o, objective_o, current, threepm, sixpm, ninepm)
    template = template_env.get_template('sales-update.json')
    data = template.render(dict(data=report))
    return FlexSendMessage(alt_text = "Sales Report "  + time, contents=BubbleContainer.new_from_json_dict(json.loads(data)))

def report(date):
    ss = client.open(Config.SPREADSHEET_NAME)
    ws = ss.get_worksheet(date.month - 1)
    totalSales = ws.acell('I' + str(date.day + 4)).value
    if totalSales:
        #The coordinates for monthObjList will always be the same regardless of current date
        monthObjList = ws.acell('G36').value
        objList = ws.acell('G' + str(date.day + 4)).value
        pastList = ws.acell('H' + str(date.day + 4)).value
        # Here we remove the commas from the values for proper integer manipulation
        objList = objList.replace(',','')
        pastList = pastList.replace(',','')
        monthObjList = monthObjList.replace(',','')
        objList = int(objList)
        pastList = int(pastList)
        # MConverting all of the values into integers  
        threepm = ws.acell('J' + str(date.day + 4)).value
        sixpm = ws.acell('K' + str(date.day + 4)).value
        ninepm = ws.acell('L' + str(date.day + 4)).value

        if threepm == '':
            threepm_o = 'TBA'
        else:
            threepm = int(threepm)
            threepm_o = str("{:,}".format(threepm)) + "円"

        if sixpm  == '':
            sixpm_o = 'TBA'
        else: 
            sixpm = int(sixpm)
            sixpm_o = str("{:,}".format(sixpm)) + "円"

        if ninepm == '':
            ninepm_o = 'TBA'
        else:
            ninepm = int(ninepm)
            ninepm_o = str("{:,}".format(ninepm)) + "円"
        
        totalSales = totalSales.replace(',','')
        totalSales = int(totalSales)
        monthlyObj = int(monthObjList)
        lastYearSales = int(pastList)
        objective = int(objList)
        # Some math
        change = int(totalSales/lastYearSales*100-100)
        changetxt = ""

        # Increases or decreases in profit comparing to last year 
        if change > 1.00:
            changetxt = "+"
        elif change < 1.00:
            changetxt = ""
        else:
            changetxt = ""
        # Whether the objective was reached or not for that day sales
        objectivestatus = ""
        if totalSales >= objective:
            objectivestatus = "REACHED"
            color_o = "#1DB446"
        elif totalSales < objective:
            objectivestatus = "NOT REACHED"
            color_o = "#FFA726"
        else:
            objectivestatus = " error"
            color_o = "#EF5350"
        # Here we append today's sales to the month dictionary to work with the variables below
        current = int(ws.acell('I36').value)
        left = int(monthlyObj) - int(current)
        percentage = int(current / monthlyObj * 100)
        # Class output variables
        objectivestatus_o = str(objectivestatus)
        date_o = date.strftime("%A, %B %d %Y")
        lastYearSales_o = str("{:,}".format(lastYearSales)) + "円"
        objective_o = str("{:,}".format(objective)) + "円"
        totalSales_o = str("{:,}".format(totalSales)) + "円"
        changetxt_o = str(changetxt)
        change_o = changetxt + str(change) + "%"
        monthlyObj_o = str("{:,}".format(monthlyObj)) +  "円"
        current_o = str("{:,}".format(current)) + "円"
        left_o = str("{:,}".format(left)) + "円"
        percentage_o = str(percentage) + "%"
        report = SalesReport(objectivestatus_o, color_o, date_o, 
            lastYearSales_o, totalSales_o, objective_o, threepm_o, 
            sixpm_o, ninepm_o, change_o, monthlyObj_o, current_o, left_o, percentage_o)
        template = template_env.get_template('sales-report.json')
        data = template.render(dict(data=report))
        # Send the structured message. Note, the template needs to be parsed to 
        # an Flex MessageUI element, in this case a BubbleContainer
        return FlexSendMessage(alt_text = "Sales Report", contents=BubbleContainer.new_from_json_dict(json.loads(data)))
    else:
        return TextSendMessage(text="Total sales missing")

import os
if __name__ == "__main__":
    port = int(Config.PORT)
    app.run(host='0.0.0.0', port=port)