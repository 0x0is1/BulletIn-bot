import discord

def tweet_embed(data):
  embed = discord.Embed(title="Twitter", color=0x11806a)
  v=''
  imgs=''
  if len(data[4]) >= 1:
    for i in data[4]:
      v+='[Read more]({0})\n'.format(i)
  message=data[1] + ' ' + v
  embed.add_field(name=data[2], value=message, inline=False)
  if len(data[5]) >= 1:
    embed.set_image(url=data[5][0])
    data[5].pop(0)
    if len(data[5])!=0:
      for i, j in enumerate(data[5]):
        imgs+='[Image[{0}]]({1})\n'.format(i, j)
      embed.add_field(name='More images: ', value=imgs, inline=False)
  
  embed.set_footer(text=data[0], icon_url=data[3])
  return embed
