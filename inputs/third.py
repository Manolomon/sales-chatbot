

# THIS IS THE THIRD INPUT SCRIPT



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
	secondInput = ws.update_acell('L5', str(inputt))
	
elif sdate == 2:
	secondInput = ws.update_acell('L6', str(inputt))

elif sdate == 3:
	secondInput = ws.update_acell('L7', str(inputt))

elif sdate == 4:
	secondInput = ws.update_acell('L8', str(inputt))

elif sdate == 5:
	secondInput = ws.update_acell('L9', str(inputt))

elif sdate == 6:
	secondInput = ws.update_acell('L10', str(inputt))

elif sdate == 7:
	secondInput = ws.update_acell('L11', str(inputt))

elif sdate == 8:
	secondInput = ws.update_acell('L12', str(inputt))

elif sdate == 9:
	secondInput = ws.update_acell('L13', str(inputt))

elif sdate == 10:
	secondInput = ws.update_acell('L14', str(inputt))
	
elif sdate == 11:
	secondInput = ws.update_acell('L15', str(inputt))
	
elif sdate == 12:
	secondInput = ws.update_acell('L16', str(inputt))

elif sdate == 13:
	secondInput = ws.update_acell('L17', str(inputt))

elif sdate == 14:
	secondInput = ws.update_acell('L18', str(inputt))
	
elif sdate == 15:
	secondInput = ws.update_acell('L19', str(inputt))

elif sdate == 16:
	secondInput = ws.update_acell('L20', str(inputt))

elif sdate == 17:
	secondInput = ws.update_acell('L21', str(inputt))
	
elif sdate == 18:
	secondInput = ws.update_acell('L22', str(inputt))

elif sdate == 19:
	secondInput = ws.update_acell('L23', str(inputt))

elif sdate == 20:
	secondInput = ws.update_acell('L24', str(inputt))

elif sdate == 21:
	secondInput = ws.update_acell('L25', str(inputt))

elif sdate == 22:
	secondInput = ws.update_acell('L26', str(inputt))

elif sdate == 23:
	secondInput = ws.update_acell('L27', str(inputt))

elif sdate == 24:
	secondInput = ws.update_acell('L28', str(inputt))

elif sdate == 25:
	secondInput = ws.update_acell('L29', str(inputt))

elif sdate == 26:
	secondInput = ws.update_acell('L30', str(inputt))

elif sdate == 27:
	secondInput = ws.update_acell('L31', str(inputt))
	
elif sdate == 28:
	secondInput = ws.update_acell('L32', str(inputt))
	
elif sdate == 29:
	secondInput = ws.update_acell('L33', str(inputt))
	
elif sdate == 30:
	secondInput = ws.update_acell('L34', str(inputt))
	
elif sdate == 31:
	secondInput = ws.update_acell('L35', str(inputt))
	
else:
	print("dateTime error")











