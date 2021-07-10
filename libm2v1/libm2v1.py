from tweepy import StreamListener
from tweepy import Stream
import tweepy, os, json

CONSUMER_KEY=os.environ.get('CK')
CONSUMER_SECRET=os.environ.get('CS')
ACCESS_KEY=os.environ.get('AK')
ACCESS_SECRET=os.environ.get('AS')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

class StdOutListener(StreamListener):

    def on_data(self, data):
        psdata=json.loads(data)
        if psdata['user']['id_str']!=ID: return
        with open('cache.json', 'w') as f:
            json.dump(psdata, f)
        print('data recieved')
        
    def on_error(self, status):
        print(status)

def parse_data(raw_data):
  timec=raw_data['created_at']
  text=raw_data['text'].split('https://t.co/')[0]
  username=raw_data['user']['name']
  prof_thumb=raw_data['user']['profile_image_url_https']
  urls, images=[], []
  for i in raw_data['entities']['urls']:
    urls.append(i['expanded_url'])
  for j in raw_data['entities']['media']:
    images.append(j['media_url_https'])
  return timec, text, username, prof_thumb, urls, images

if __name__ == '__main__':
    api = tweepy.API(auth)
  
    # the screen name of the user
    screen_name = "0x0is1"
  
    # fetching the user
    user = api.get_user(screen_name)
  
    # fetching the ID
    global ID
    ID = user.id_str
    print(ID)
    listener = StdOutListener()
    twitterStream = Stream(auth, listener)
    twitterStream.filter(follow=[ID])
    
