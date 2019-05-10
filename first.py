
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

ss = client.open("database")

date = datetime.datetime.now()

# I had to make a new "integer" variable because I don't know how to code properly, lol 

fMonth = date.strftime("%m")
sMonth = int(fMonth)

fYear = date.strftime("%y")
sYear = int(fYear)




app = Flask(__name__)


line_bot_api = LineBotApi('pDGDz4DzoDyeCQccYHoWMD+h2JUs+myycFqVVrOLV075PVxrGdVV20nMtYqU2BPZryOzofwipzEtPndQifjWSSPrFyy6Jzwv/gWoozGUQDGMJlyVltL0BTaqqfLhjRjlbLxQoKRnEstaw0demRT8VwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9a34a6b435e9799517fe0f238c487760')
line_bot_api = LineBotApi(config.CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(config.CHANNEL_SECRET)


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


line_bot_api.push_message("U8e75ea0a470e2e8b02d8e7116fe13d7f", TextSendMessage(text="3 PM Test Message"))






if sMonth == 1:
	ws = ss.worksheet('January') 

elif sMonth == 2:
	ws = ss.worksheet('February') 

elif sMonth == 3:
	ws = ss.worksheet('March') 

elif sMonth == 4:
	ws = ss.worksheet('April') 

elif sMonth == 5:
	ws = ss.worksheet('May') 

elif sMonth == 6:
	ws = ss.worksheet('June') 

elif sMonth == 7:
	ws = ss.worksheet('July') 

elif sMonth == 8:
	ws = ss.worksheet('August') 

elif sMonth == 9:
	ws = ss.worksheet('September') 

elif sMonth == 10:
	ws = ss.worksheet('October') 

elif sMonth == 11:
	ws = ss.worksheet('November') 

elif sMonth == 12:
	ws = ss.worksheet('December') 



# Day loop

fdate = date.strftime("%d")
sdate = int(fdate)



if sdate == 1:
	firstInput = ws.update_acell('J5', str(inputt))
	
elif sdate == 2:
	firstInput = ws.update_acell('J6', str(inputt))

elif sdate == 3:
	firstInput = ws.update_acell('J7', str(inputt))

elif sdate == 4:
	firstInput = ws.update_acell('J8', str(inputt))

elif sdate == 5:
	firstInput = ws.update_acell('J9', str(inputt))

elif sdate == 6:
	firstInput = ws.update_acell('J10', str(inputt))

elif sdate == 7:
	firstInput = ws.update_acell('J11', str(inputt))

elif sdate == 8:
	firstInput = ws.update_acell('J12', str(inputt))

elif sdate == 9:
	firstInput = ws.update_acell('J13', str(inputt))

elif sdate == 10:
	firstInput = ws.update_acell('J14', str(inputt))
	
elif sdate == 11:
	firstInput = ws.update_acell('J15', str(inputt))
	
elif sdate == 12:
	firstInput = ws.update_acell('J16', str(inputt))

elif sdate == 13:
	firstInput = ws.update_acell('J17', str(inputt))

elif sdate == 14:
	firstInput = ws.update_acell('J18', str(inputt))
	
elif sdate == 15:
	firstInput = ws.update_acell('J19', str(inputt))

elif sdate == 16:
	firstInput = ws.update_acell('J20', str(inputt))

elif sdate == 17:
	firstInput = ws.update_acell('J21', str(inputt))
	
elif sdate == 18:
	firstInput = ws.update_acell('J22', str(inputt))

elif sdate == 19:
	firstInput = ws.update_acell('J23', str(inputt))

elif sdate == 20:
	firstInput = ws.update_acell('J24', str(inputt))

elif sdate == 21:
	firstInput = ws.update_acell('J25', str(inputt))

elif sdate == 22:
	firstInput = ws.update_acell('J26', str(inputt))

elif sdate == 23:
	firstInput = ws.update_acell('J27', str(inputt))

elif sdate == 24:
	firstInput = ws.update_acell('J28', str(inputt))

elif sdate == 25:
	firstInput = ws.update_acell('J29', str(inputt))

elif sdate == 26:
	firstInput = ws.update_acell('J30', str(inputt))

elif sdate == 27:
	firstInput = ws.update_acell('J31', str(inputt))
	
elif sdate == 28:
	firstInput = ws.update_acell('J32', str(inputt))
	
elif sdate == 29:
	firstInput = ws.update_acell('J33', str(inputt))
	
elif sdate == 30:
	firstInput = ws.update_acell('J34', str(inputt))
	
elif sdate == 31:
	firstInput = ws.update_acell('J35', str(inputt))
	
else:
	print("dateTime error")











