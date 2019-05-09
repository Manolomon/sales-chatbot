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