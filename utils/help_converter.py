import discord
from discord.ext import commands
from discord import Embed

fields = [
    ("","",True)
  ]

def Utility(ctx):
  embed = Embed(description=f"**Utility Commands**",color=0xffffff)#\n\n`sleep:` set my or member timer disconnect voice channel\n\n`poll [message]:` poll in your server",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)

  fields = [
    ("sleep","```yaml\n.sleep <duration> [member]```",True),
    ("sleep delete","```yaml\n.sleep delete [member]```",True),
    ("poll","```yaml\n.poll [message]```",True),
    ("binary","```yaml\n.binary [message]```",True),
    ("reverse","```yaml\n.reverse [message]```",True),
    ("translate","```yaml\n.trans <output language> [messsage]```",True)
  ]
                          
  for name, value, inline in fields:
    embed.add_field(name=name, value=value, inline=inline)

  return embed

def Infomation(ctx):
  embed = Embed(description="**Infomation Commands**",color=0xffffff)#\n\n`userinfo , ui [targer]` : show userinfo infomation\n\n`serverinfo , si` : show server infomation\n\n`avatar , av [targer]` : show my avatar profile or target\n\n`servericon` `sic` : show server icon\n\n`serverbanner` , `sb` : show server server banner\n\n`invitebanner` , `ss` : show server splash(invite banner)",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)

  fields = [
    ("Userinfo","```yaml\n.ui [member]```",True),
    ("Serverinfo","```yaml\n.serverinfo | .si```",True),
    ("Avatar","```yaml\n.avatar [member]```",True),
    ("Server Icon","```yaml\n.servericon | .sic```",True),
    ("Server Banner","```yaml\n.serverbanner | .sb```",True),
    ("Server Splash","```yaml\n.splash | .ss```",True),
    ("Emoji Info","```yaml\n.emojinfo [emoji] | .ei [emoji]```",True),

  ]

  for name, value, inline in fields:
    embed.add_field(name=name, value=value, inline=inline)

  return embed

def Moderation(ctx):
  embed = Embed(description="**Moderation Commands**",color=0xffffff)#\n\n`clear [number] or all` : clear message\n\n`muterole` : create muterole\n\n`mute [target] [time]` : mute member\n\n`unmute [target]` : unmute member\n\n`kick [target]` : kick member\n\n`ban [target]` : ban member\n\n`unban [target]` : unban member\n\n`lockdown` : lock or unlock text channel\n\n`nick [member] ` : change nickname member\n\n`slowmode [seconds]` : set slowmode in channel",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)
  
  fields = [
    ("Clear","```yaml\n.clear <amount>```",True),
    ("Mute Role","```yaml\n.muterole```",True),
    ("Mute","```yaml\n.mute [member] <duration>```",True),
    ("Unmute","```yaml\n.unmute [member]```",True),
    ("Kick","```yaml\n.kick [member]```",True),
    ("Ban","```yaml\n.ban [member]```",True),
    ("Unban","```yaml\n.unban [member]```",True),
    ("Lockdown","```yaml\n.lock [channel]```",True),
    ("Slowmode","```yaml\n.slow <duration>```",True),
    ("Change Nickname","```yaml\n.nick [member] <name>```",True)

  ]

  for name, value, inline in fields:
    embed.add_field(name=name, value=value, inline=inline)
  
  return embed

def Giveaway(ctx):
  embed = Embed(description="**Giveaway Commands**",color=0xffffff)#\n\n`giveaway , g `: The group command for managing giveaways\n\n`reroll :` reroll giveaway",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)

  fields = [
    ("Giveaway","```yaml\n.g```",True),
    ("Reroll","```yaml\n.reroll```",True),
  ]

  for name, value, inline in fields:
    embed.add_field(name=name, value=value, inline=inline)
  
  return embed
  
def Fun(ctx):
  embed = Embed(description="**Fun Commands**",color=0xffffff)#\n\n`ani` , `ani list`: random anime images or specify list\n\n`cat` : random cat images\n\n`fox` : random fox images\n\n`gif[search]` : random gif or search\n\n`bm [message]` : Let the bot send the message\n\n`owo [message]` : Any message to owo",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)

  fields = [
    ("Anime gif","```yaml\n.ani | .ani list```",True),
    ("Cat","```yaml\n.cat```",True),
    ("Fox","```yaml\n.fox```",True),
    ("Gif","```yaml\n.gif <keyword> or random```",True),
    ("OwO","```yaml\n.owo [message]```",True),
    ("Echo","```yaml\n.echo [message]```",True),
    ("Saybot","```yaml\n.saybot [message]```",True),
    ("Member Saybot","```yaml\n.saybotm [member] [message]```",True),

  ]

  for name, value, inline in fields:
    embed.add_field(name=name, value=value, inline=inline)
  
  return embed

def Meta(ctx):
  embed = Embed(description="**Meta Commands**",color=0xffffff)#\n\n`ping`: check latency bot\n\n`invite` : invite the bot!!\n\n`feedback` : send message to bot developer\n\n`support` : Get the invite link for the support server!\n\n`vote :`  Get the voting link for the bot",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)

  fields = [
    ("Bot Latency","```yaml\n.ping```",True),
    ("Invite Bot","```yaml\n.invite```",True),
    ("Feedback","```yaml\n.feedback```",True),
    ("Request","```yaml\n.req```",True),

  ]

  for name, value, inline in fields:
    embed.add_field(name=name, value=value, inline=inline)
  
  return embed

def Reaction(ctx):
  embed = Embed(description="**Reaction Roles**\n\n <a:a_dp_heart2:875170744722653245> **__c o l o r s__** <a:bw_white_Hearts_White:859399024558080020> : <#840380566862823425>",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)  
  return embed

def Leveling(ctx):
  embed = Embed(description="**Leveling**\n\nAutomationl add experience\nyou can get experience in :\n  <#861883647070437386> <#840398821544296480> <#859960606761549835>",color=0xffffff)#\n\n`xp [member]` : check my level or member\n\n`rank` : show ranking level all member",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)

  fields = [
    ("XP","```yaml\n.xp [member]```",True),
    ("Ranking","```yaml\n.rank```",True),
  ]

  for name, value, inline in fields:
    embed.add_field(name=name, value=value, inline=inline)
  
  return embed

def NSFW(ctx):
  embed = Embed(description="**NSFW Commands**\n\n*NSFW* is alollowed in <#850507964938715196>",color=0xffffff)#\n\n`hentai` : hentai picture or gif\n\n",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)

  fields = [
    ("Hentai GIF","```yaml\n.hentai```",True),
  ]

  for name, value, inline in fields:
    embed.add_field(name=name, value=value, inline=inline)
  
  return embed
