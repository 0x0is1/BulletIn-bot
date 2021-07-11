def parse_data(raw_data):
  timec=raw_data['created_at']
  text=raw_data['text'].split('https://t.co/')[0]
  username=raw_data['user']['name']
  prof_thumb=raw_data['user']['profile_image_url_https']
  urls, images=[], []
  for i in raw_data['entities']['urls']:
    urls.append(i['expanded_url'])
  try:
    for j in raw_data['entities']['media']:
      images.append(j['media_url_https'])
  except KeyError:pass

  return timec, text, username, prof_thumb, urls, images

def fetch_user(username, api):
  return api.get_user(username)
