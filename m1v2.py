from discord.ext import commands, tasks
import tweepy, discord, json, asyncio
from tweepy import StreamListener, Stream
from configuration import *
from libm2v1.libm2v1 import parse_data, fetch_user

contents = {}
follow_handles = ['0x0is1']
follow_handles_ids = []
info = {}
REFRESH_TIME=5

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
bot = commands.Bot(command_prefix='??')

for i in follow_handles:
  fhid=fetch_user(i, api).id_str
  follow_handles_ids.append(fhid)
  if fhid not in list(info.keys()):
	  info[fhid]=[]
	  


class StdOutListener(StreamListener):
	def on_data(self, data):
		data = json.loads(data)
		try:
			curr_id = data['user']['id_str']
			if curr_id not in follow_handles_ids: return
		except KeyError:
			return

		parsed_data = parse_data(data)
		contents[curr_id] = list(parsed_data)
		print(contents)

	def on_error(self, status):
		print(status)


@tasks.loop(seconds=REFRESH_TIME)
async def auto_sender():
	if len(contents) == 0: return
	if len(info) == 0: return
	tids = list(contents.keys())
	for tid in tids:
		for cid in info[tid]:
			channel = bot.get_channel(cid)
			await channel.send(contents[tid])
			contents.pop(tid)
      
@bot.event
async def on_ready():
  print('Bot status: online')
  auto_sender.start()
  listener = StdOutListener()
  twitterStream = Stream(auth, listener)
  twitterStream.filter(follow=follow_handles_ids, is_async=True)

@bot.command()
async def subscribe(ctx):
	message = 'Choose handles from following options.\n'
	for i, j in enumerate(follow_handles):
		message += str(i) + '. ' + j + '\n'
	message += 'Write all handle numbers with a space in 30 seconds:'
	await ctx.send(message)
	try:
		msg = await bot.wait_for("message", timeout=30)
		for i in msg.content.split(' '):
			tid = fetch_user(follow_handles[int(i)], api).id_str
			channel_id = ctx.message.channel.id
			info[tid].append(channel_id)
		with open('info.json', 'w') as f:
			json.dump(info, f)
		await ctx.send('**Subscribed.**')
	except asyncio.TimeoutError:
		await ctx.send("Sorry, you didn't reply in time!")

@bot.command()
async def unsubscribe(ctx):
	message = 'Choose handles from following options.\n'
	for i, j in enumerate(follow_handles):
		message += str(i) + '. ' + j + '\n'
	message += 'Write all handle numbers with a space in 30 seconds:'
	await ctx.send(message)
	try:
		msg = await bot.wait_for("message", timeout=30)
		for i in msg.content.split(' '):
			tid = fetch_user(follow_handles[int(i)], api).id_str
			channel_id = ctx.message.channel.id
			info[tid].remove(channel_id)
		with open('info.json', 'w') as f:
			json.dump(info, f)
		await ctx.send('**Unsubscribed.**')
	except asyncio.TimeoutError:
		await ctx.send("Sorry, you didn't reply in time!")
  except KeyError:pass

bot.run(BOT_TOKEN)
