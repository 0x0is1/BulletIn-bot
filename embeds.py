import discord

def tweet_embed(data):
  embed = discord.Embed(color=0x11806a)
  imgs=''
  message=data[1]
  embed.add_field(name=data[2], value=message, inline=False)
  if len(data[4]) >= 1:
    embed.set_image(url=data[4][0])
    data[4].pop(0)
    if len(data[4])!=0:
      for i, j in enumerate(data[4]):
        imgs+='[Image[{0}]]({1})\n'.format(i, j)
      embed.add_field(name='More images: ', value=imgs, inline=False)
  
  embed.set_footer(text=data[0], icon_url=data[3])
  return embed
