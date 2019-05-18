import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    CHANNEL_ACCESS_TOKEN = os.environ.get('CHANNEL_ACCESS_TOKEN')
    CHANNEL_SECRET = os.environ.get('CHANNEL_SECRET')
    PORT = os.environ.get('PORT', 5000)
    GROUP_ID = os.environ.get('GROUP_ID')
    SPREADSHEET_NAME = os.environ.get('SPREADSHEET_NAME')
