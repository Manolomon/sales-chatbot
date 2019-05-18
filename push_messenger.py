#!/venv/bin/python

from linebot import LineBotApi
from linebot.models import (
    FlexSendMessage, TextSendMessage
)
import sys

from config import Config

# Channel Access Token
line_bot_api = LineBotApi(Config.CHANNEL_ACCESS_TOKEN)

def ask_for_input_push_message(content):
    line_bot_api.push_message(Config.GROUP_ID, TextSendMessage(text=content))

if __name__ == "__main__":
    ask_for_input_push_message(sys.argv[1])
