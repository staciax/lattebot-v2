import discord
from discord.ext import commands
from discord import Embed

def Utility(ctx):
  embed = Embed(description=f"**Utility Commands**\n\n`sleep [time] [member]:` set my or member timer disconnect voice channel\n\n`poll [message]:` poll in your server",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)
  return embed

def Infomation(ctx):
  embed = Embed(description="**Infomation Commands**\n\n`userinfo , ui [targer]` : show userinfo infomation\n\n`serverinfo , si` : show server infomation\n\n`avatar , av [targer]` : show my avatar profile or target\n\n`servericon` `sic` : show server icon\n\n`serverbanner` , `sb` : show server server banner\n\n`invitebanner` , `ss` : show server splash(invite banner)",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)
  return embed

def Moderation(ctx):
  embed = Embed(description="**Moderation Commands**\n\n`clear [number] or all` : clear message\n\n`muterole` : create muterole\n\n`mute [target] [time]` : mute member\n\n`unmute [target]` : unmute member\n\n`kick [target]` : kick member\n\n`ban [target]` : ban member\n\n`unban [target]` : unban member\n\n`lockdown` : lock or unlock text channel\n\n`nick [member] ` : change nickname member\n\n`slowmode [seconds]` : set slowmode in channel",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)
  return embedf

def Giveaway(ctx):
  embed = Embed(description="**Giveaway Commands**\n\n`giveaway , g `: The group command for managing giveaways\n\n`reroll :` reroll giveaway",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)
  return embed
  
def Fun(ctx):
  embed = Embed(description="**Fun Commands**\n\n`ani` , `ani list`: random anime images or specify list\n\n`cat` : random cat images\n\n`fox` : random fox images\n\n`gif[search]` : random gif or search\n\n`bm [message]` : Let the bot send the message\n\n`owo [message]` : Any message to owo",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)
  return embed

def Meta(ctx):
  embed = Embed(description="**Meta Commands**\n\n`ping`: check latency bot\n\n`invite` : invite the bot!!\n\n`feedback` : send message to bot developer\n\n`support` : Get the invite link for the support server!\n\n`vote :`  Get the voting link for the bot",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)
  return embed

def Reaction(ctx):
  embed = Embed(description="**Reaction Roles**\n\n <a:a_dp_heart2:875170744722653245> **__c o l o r s__** <a:bw_white_Hearts_White:859399024558080020> : <#840380566862823425>",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)
  return embed

def Leveling(ctx):
  embed = Embed(description="**Leveling**\n\nAutomationl add experience\nyou can get experience in :\n  <#861883647070437386> <#840398821544296480> <#859960606761549835>\n\n`xp [member]` : check my level or member\n\n`rank` : show ranking level all member",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)
  return embed

def NSFW(ctx):
  embed = Embed(description="**NSFW Commands**\n\n*NSFW* is alollowed in <#850507964938715196>\n\n`hentai` : hentai picture or gif\n\n",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)
  return embed
