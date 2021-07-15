import re
def parse_data(raw_data):
  try:
    raw_data = raw_data['retweeted_status']
  except KeyError:pass
  timec=raw_data['created_at'].replace(' +0000', '')
  username=raw_data['user']['name']
  prof_thumb=raw_data['user']['profile_image_url_https']
  
  try:
    raw_data=raw_data['extended_tweet']
    text=raw_data['full_text']
  except KeyError:
    text=raw_data['text']
  images=[]
  try:
    for j in raw_data['entities']['media']:
      images.append(j['media_url_https'])
  except KeyError:pass
  urls = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+', text)
  for i in range((len(urls) - len(images))):
    try:
      text=text.replace(urls[i], '[Visit]({0})'.format(urls[i]))
      urls.pop(i)
    except IndexError:pass
  for j in urls:
    text=text.replace(j, '')
  return timec, text, username, prof_thumb, images

def fetch_user(username, api):
  return api.get_user(username)
