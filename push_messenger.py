#!/venv/bin/python

from linebot import LineBotApi
from linebot.models import (
    FlexSendMessage, TextSendMessage
)
from linebot.models import BubbleContainer

from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
import sys

import config
from sales_report import SalesReport

line_bot_api = LineBotApi(config.Config.CHANNEL_ACCESS_TOKEN)
template_env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml', 'json'])
)

def input_push_message(content):
    line_bot_api.push_message(config.Config.GROUP_ID, 
        TextSendMessage(text=content))

def report_push_message():
    data = SalesReport();
    template = template_env.get_template('sales-report.json')
    data = template.render(dict(data=data))
    message = FlexSendMessage(alt_text = "Sales Report", 
        contents=BubbleContainer.new_from_json_dict(json.loads(data)))
    line_bot_api.push_message(config.Config.GROUP_ID, message)

if __name__ == "__main__":
    if sys.argv[1] == 'input':
        input_push_message(sys.argv[2])
    if sys.argv[1] == 'report':
        report_push_message()
