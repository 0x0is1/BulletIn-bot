import discord

def tweet_embed(data):
  embed = discord.Embed(title=data[2], color=0x11806a)
  embed.set_thumbnail(url=data[3])
  embed.add_field(name='Message: ', value=data[1], inline=False)
  v=''
  imgs=''
  if len(data[4]) >= 1:
    for i, j in enumerate(data[4]):
      v+='[Read more[{0}]]({1})\n'.format(i, j)
    embed.add_field(name='Visit: ', value=v, inline=False)
    
  if len(data[5]) >= 1:
    embed.set_image(url=data[5][0])
    data[5].pop(0)
    if len(data[5])!=0:
      for i, j in enumerate(data[5]):
        imgs+='[Image[{0}]]({1})\n'.format(i, j)
      embed.add_field(name='More images: ', value=imgs, inline=False)
  
  embed.set_footer(text=data[0])
  return embed
