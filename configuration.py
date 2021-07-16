import os, json

CONSUMER_KEY = os.environ.get('CK')
CONSUMER_SECRET = os.environ.get('CS')
ACCESS_KEY = os.environ.get('AK')
ACCESS_SECRET = os.environ.get('AS')
BOT_TOKEN = os.environ.get('EXPERIMENTAL_BOT_TOKEN')
with open('handles.json', 'r') as f:
  follow_handles = json.load(f)['handles']
