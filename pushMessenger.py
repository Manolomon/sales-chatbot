from linebot import LineBotApi
from linebot.models import TextSendMessage
import sys

import config

line_bot_api = LineBotApi('pDGDz4DzoDyeCQccYHoWMD+h2JUs+myycFqVVrOLV075PVxrGdVV20nMtYqU2BPZryOzofwipzEtPndQifjWSSPrFyy6Jzwv/gWoozGUQDGMJlyVltL0BTaqqfLhjRjlbLxQoKRnEstaw0demRT8VwdB04t89/1O/w1cDnyilFU=')


def input_push_message(content):
    line_bot_api.push_message('U8e75ea0a470e2e8b02d8e7116fe13d7f', 
        TextSendMessage(text=content))


if __name__ == "__main__":
    input_push_message(sys.argv[1])
