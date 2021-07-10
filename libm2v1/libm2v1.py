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
        if psdata['id'] != 96900937:
          return
        with open('cache.json', 'w') as f:
            json.dump(psdata, f)
        print('data recieved')
        
    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    api = tweepy.API(auth)
  
    # the screen name of the user
    screen_name = "ndtvfeed"
  
    # fetching the user
    user = api.get_user(screen_name)
  
    # fetching the ID
    ID = user.id_str
    print(ID)
    listener = StdOutListener()
    twitterStream = Stream(auth, listener)
    twitterStream.filter(follow=[ID])
  
