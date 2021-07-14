import re
def parse_data(raw_data):
  timec=raw_data['created_at'].replace(' +0000', '')
  text=raw_data['text']
  urls = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+', text)
  for i in urls:
    text=text.replace(i, '\n[Visit]({0})'.format(i))
  username=raw_data['user']['name']
  prof_thumb=raw_data['user']['profile_image_url_https']
  images=[]
  
  try:
    for j in raw_data['entities']['media']:
      images.append(j['media_url_https'])
  except KeyError:pass

  return timec, text, username, prof_thumb, images

def fetch_user(username, api):
  return api.get_user(username)
