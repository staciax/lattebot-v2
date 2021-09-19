import discord
from discord.ext import commands
from discord import Embed

fields = [
    ("","",True)
  ]

def Utility(ctx):
  embed = Embed(description=f"**Utility Commands**",color=0xffffff)#\n\n`sleep:` set my or member timer disconnect voice channel\n\n`poll [message]:` poll in your server",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)
  
  description="""
  Use `.help <command>` for more informations about a command.

  `sleep` • Set timer disconnect voice channel.
  `sleep stop` • Stop sleep timer.
  `poll` • Create poll.
  `binary` • Text to binary.
  `reverse , sb` • Reverse text.
  `translate , trans` • Translate message.
  `random_number , rn` • Random number Lowest - Highest.
  """
  embed.description = description

  return embed

def Infomation(ctx):
  embed = Embed(title="**Infomation Commands**",color=0xffffff)

  description="""
  Use `.help <command>` for more informations about a command.

  `userinfo , ui` • Show user infomation.
  `serverinfo , si` • Show serverinfo infomation.
  `avatar , av` • Display avatar.
  `banner , bn` • Display banner.
  `servericon , sic` • Display Server icon.
  `serverbanner , sb` • Display server banner.
  `splash , ss` • Display server splash.
  `emojinfo , ei` • Show emojinfo.
  `roleinfo , ri` • Show roleinfo.
  """
  embed.description = description
  
  return embed

def Moderation(ctx):
  embed = Embed(title="Moderation Commands",color=0xffffff)
  
  description="""
  Use `.help <command>` for more informations about a command.

  `clear` • clear message
  `muterole` • create mute role
  `mute` • mute member 
  `unmute` • unmute member 
  `kick` • kick member
  `ban` • ban member
  `lock` • lockdown channel
  `slow` • slowmode channel
  `nick` • change nickname member

  """
  embed.description = description
  
  return embed

def Giveaway(ctx):
  embed = Embed(title="Giveaway Commands",color=0xffffff)

  description="""
  Use `.help <command>` for more informations about a command.

  `g` • Start create giveaway.
  `reroll` • Reroll giveaway.
  """
  embed.description = description
  
  return embed
  
def Fun(ctx):
  embed = Embed(title="Fun Commands",color=0xffffff)
  
  description = """
  Use `.help <command>` for more informations about a command.
  
 
  • `owo`, `echo` ,`saybot`, `saybotm`
  """
  embed.description = description
  
  return embed

def Anime(ctx):
  embed = Embed(title="Anime Commands",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)

  description="""
  Use `.help <command>` for more informations about a command.
    
  • `waifu`, `waifu2`, `bonk`, `bully`, `blush` ,`bite`, `cry`, `happy`, `kiss`, `kicks`, `lick`, `neko` , `nom` , `maid`, `pat` , `smug` , `slap` , `smile` , `wink`
  """
  embed.description = description
  
  return embed

def Meta(ctx):
  embed = Embed(title="Meta Commands",color=0xffffff)
  
  description="""
  Use `.help <command>` for more informations about a command.

  `ping` • Show latency bot.
  `invite` • Invite bot.
  `feedback` • Your feedback for bot .
  `req` • Your request.
  """
  embed.description = description
  
  return embed

def Reaction(ctx):
  embed = Embed(description="**Reaction Roles**\n\n <a:a_dp_heart2:875170744722653245> **__c o l o r s__** <a:bw_white_Hearts_White:859399024558080020> : <#840380566862823425>",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)  
  return embed

def Leveling(ctx):
  embed = Embed(title="Leveling",color=0xffffff)

  description="""
  Use `.help <command>` for more informations about a command.

  Automationl add experience
  you can get experience in :
  <#861883647070437386> <#840398821544296480> <#859960606761549835> <#863438518981361686>

  `xp` • Show my xp.
  `rank` • Show ranking board.
  """
  embed.description = description
  
  return embed

def NSFW(ctx):
  embed = Embed(title="NSFW Commands",color=0xffffff)

  description = """
  Use `.help <command>` for more informations about a command.
  
  *NSFW* is alollowed in <#850507964938715196>
  
  • `waifu` , `neko` , `trap` , `blowjob` , `ass`, `ecchi`, `ero`, `hentai` ,`hmaid`, `milf`, `oppai`, `oral`, `paizuri`, `selfies`, `uniform`
  """
  # `ass`, `ecchi`, `ero`, `hentai` ,`maid`, `milf`, `oppai`, `oral`, `paizuri`, `selfies`, `uniform` , 
  embed.description = description
  
  return embed

def Help_image(ctx):
  embed = Embed(title="Image Commands",color=0xffffff)

  description = """
  Use `.help <command>` for more informations about a command.
  
  • `cat` , `fox` , `gif` , 
  """

  embed.description = description
  
  return embed
