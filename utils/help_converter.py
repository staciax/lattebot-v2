import discord
from discord.ext import commands
from discord import Embed
from utils import emoji_converter

from config import *

fields = [
    ("","",True)
  ]

def Utility():
  embed = Embed(title=f"⚙️ Utility Commands",color=0xffffff)
  description="""
  Use `.help <command>` for more informations about a command.

  `afk` • set your afk
  `sleep` • Set timer disconnect voice channel.
  `snipe` • Snipe message after delete
  `remind`• timer remind me
  `poll` • Create poll.
  `binary` • Text to binary.
  `reverse` • Reverse text.
  `translate , trans` • Translate message.
  `random` • randrom a range.
  `random_number , rn` • Random number Lowest - Highest.
  `random_invoice`, rnv • Random member in your current VC
  `platform` , pt • What platform are your/members online on?
  `number_to_roman` , ntr • Convert roman to number
  `roman_to_number` , rtn • Convert number to roman
  """
  embed.description = description

  return embed

def Infomation():
  embed = Embed(title=f"{emoji_converter('ShinoSmirk')} **Infomation Commands**",color=0xffffff)

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

def Moderation():
  embed = Embed(title=f"{emoji_converter('moderation')} Moderation Commands",color=0xffffff)
  
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
  `audit` • view audit-log
  `createemoji` • crate emoji with link
  `deleteemoji` • delete emoji

  """
  embed.description = description
  
  return embed

def Giveaway():
  embed = Embed(title="🎉 Giveaway Commands",color=0xffffff)

  description="""
  Use `.help <command>` for more informations about a command.

  `g` • Start create giveaway.
  `reroll` • Reroll giveaway.
  """
  embed.description = description
  
  return embed
  
def Fun():
  embed = Embed(title="🥳 Fun Commands",color=0xffffff)
  
  description = """
  Use `.help <command>` for more informations about a command.
  
 
  • `owo`, `echo` ,`saybot`, `saybotm`, `valorant`, `apex`, `genshinmap , gsmap`
  """
  embed.description = description
  
  return embed

def Anime():
  embed = Embed(title=f"{emoji_converter('miraishocked')} Anime Commands",color=0xffffff)

  description="""
  Use `.help <command>` for more informations about a command.
    
  • `waifuall`,`waifu`, `waifu2`, `awoo`, `bonk`, `bully`, `blush` ,`bite`, `cry`, `cuddle`, `cringe`, `dance`, `glomp`, `happy`, `highfive`, `handhold`, `kiss`, `kill`, `kicks`, `lick`, `neko` , `nom` , `maid`, `megumin`, `pat`, `pokes` , `smug` , `shinobu` , `slap` , `smile` , `wink`, `wave`, `yeet`
  """
  embed.description = description
  
  return embed

def Meta():
  embed = Embed(title=f"{emoji_converter('Ani1')} Meta Commands",color=0xffffff)
  
  description="""
  Use `.help <command>` for more informations about a command.

  `about` • Sbout me.
  `ping` • latency bot.
  `invite` • Invite bot.
  `feedback` • Your feedback for me.
  `req` • Your request.
  """
  embed.description = description
  
  return embed

def Reaction():
  embed = Embed(title=f"{emoji_converter('chocolawow')} Reaction Roles",description="<a:a_dp_heart2:875170744722653245> **__c o l o r s__** <a:bw_white_Hearts_White:859399024558080020> : <#840380566862823425>",color=0xffffff)
  return embed

def Leveling():
  embed = Embed(title=f"{emoji_converter('ClevelandDeal')} Leveling",color=0xffffff)

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

def NSFW():
  embed = Embed(title=f"{emoji_converter('Aoba')} NSFW Commands",color=0xffffff)

  description = """
  Use `.help <command>` for more informations about a command.
  
  *NSFW* is alollowed in <#850507964938715196>
  
  • `waifu` , `neko` , `trap` , `blowjob` , `ass`, `ecchi`, `ero`, `hentai` ,`hmaid`, `milf`, `oppai`, `oral`, `paizuri`, `selfie`, `uniform`
  """
  # `ass`, `ecchi`, `ero`, `hentai` ,`maid`, `milf`, `oppai`, `oral`, `paizuri`, `selfies`, `uniform` , 
  embed.description = description
  
  return embed

def Help_image():
  embed = Embed(title=f"{emoji_converter('image')} Image Commands",color=0xffffff)

  description = """
  Use `.help <command>` for more informations about a command.
  
  • `cat` , `fox` , `gif` , 
  """

  embed.description = description
  
  return embed

def Help_tag():
  embed = Embed(title=f"{emoji_converter('amelia')} Tag Commands",color=0xffffff)

  description = """
  Use `.help <command>` for more informations about a command.
  """
  embed.description = description
  embed.add_field(name="tag", value=f"```css\n{PREFIX}tag <name>```",inline=False)
  embed.add_field(name="tag add : เพิ่ม", value=f"```css\n{PREFIX}tag add <name> <message>```",inline=False)
  embed.add_field(name="tag remove : ลบออก", value=f"```css\n{PREFIX}tag remove <name>```",inline=False)
  embed.add_field(name="tag list : ตรวจสอบรายการ", value=f"```css\n{PREFIX}tag list```",inline=False)
  embed.add_field(name="tag edit : แก้ไขข้อความ", value=f"```css\n{PREFIX}tag edit <name> <message>```",inline=False)
  embed.add_field(name="tag alias : แก้ไขชื่อ", value=f"```css\n{PREFIX}tag alias <old name> <new name>```",inline=False)
  embed.add_field(name="tag search : ค้นหา", value=f"```css\n{PREFIX}tag search <name>```",inline=False)
  
  return embed
