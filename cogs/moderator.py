# Standard 
import discord
import datetime
import asyncio
import json
from discord.ext import commands
from datetime import datetime, timedelta, timezone


# Third party
from re import search
# Local
import utils
from config import *

intents = discord.Intents()
intents.all()
intents.members = True 
intents = discord.Intents(messages=True, guilds=True)

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client        
#        self.url_regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
#        self.links_allowed = (861874852050894868,)
#        self.images_allowed = (861874852050894868,)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
        while True:
#            print("spam detct")
            await asyncio.sleep(10)
            with open("data/spam_detect.txt", "r+") as file:
                file.truncate(0)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels, name=WELCOME)
        if channel:
            embed=discord.Embed(
        description=f"ʚ˚̩̥̩ɞ ◟‧Welcome‧ *to* **{member.guild}!** <a:ab__purplestar:854958903656710144>\n　。\nෆ ₊˚don’t forget to check out . . .\n\n‧˚₊ ପ <:a_pink_dot:860493678723072000>︰<#861774918290636800> ଓ ♡ ˖˚˳\n♡ ꒷ get latte roles~︰𓂃 ꒱\n\n⸝⸝﹒{member.mention} ꒱ <a:S_wtfemoji:860490611048054845>", #⊹₊˚**‧Welcome‧**˚₊⊹ 
        timestamp=datetime.now(timezone.utc),
        color=0xc4cfcf
    
        )
        embed.set_author(name=f"{member}", icon_url=member.avatar.url), 
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_footer(text=f"You're our {member.guild.member_count} members ෆ"),

        await channel.send(embed=embed) #(content=f"||{member.mention}||", embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.text_channels, name=LEAVE)
        if channel:
            embed = discord.Embed(
                description=f"**Leave Server\n`{member}`**",
                color=0xdbd7d2)
            embed.set_footer(text="—・see ya good bye")
            embed.timestamp = datetime.now(timezone.utc)

        await channel.send(embed = embed)  #await channel.send(f"{member} has left the server")

    @commands.command(description="ban member")
    @commands.guild_only()
    @commands.has_permissions(administrator = True)
#    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        embed = discord.Embed(title="Banned Member", description=f'{member.name}#{member.discriminator} has been banned from server\nReason: {reason}',timestamp=datetime.now(timezone.utc),color=0xffffff)
        embed.set_footer(text=f"Banned by {ctx.author}" , icon_url = ctx.author.avatar.url)

        embedprm = discord.Embed(title="Ban Error\n", description="`Bot doesn't have enough permission to ban someone.`",color=0xffffff)
       
        try:
            await member.ban(reason=reason)
            await ctx.message.delete()
            await ctx.channel.send(embed=embed)
        except Exception:
            await ctx.channel.send(embed=embedprm)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True) 
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            embedub = discord.Embed(title="Unbanned Member\n", description=f"You has been unbanned : {user.mention} !",color=0xffffff)

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(embed=embedub)

    @commands.command(name="kick", description="kick member", pass_context=True)
    @commands.has_permissions(kick_members=True)
    @commands.guild_only()
    async def kick(self, ctx, member: discord.Member, *, reason=None):

        embedkick = discord.Embed(title="Kicked Member", description=f'Member {member.mention} has been Kicked\nReason : {reason}',color=0xffffff)

        await member.kick(reason=reason)
        await ctx.send(embed=embedkick)
    
    @commands.command(description="clear message")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: str):
        if amount == 'all':
             await ctx.channel.purge()
        else:
            await ctx.channel.purge(limit=(int(amount) + 1))

    @commands.command(description="mute member")
    @commands.has_permissions(administrator = True)
    @commands.guild_only()
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(ctx.guild.roles, name=MUTEROLE)

        if not mutedRole:
            mutedRole = await guild.create_role(name=MUTEROLE , colour=discord.Colour(COLORMUTE))
            embedcreate = discord.Embed(title="BOT SETTING UP",description=f"`your server don't have` **`Muted Role`**\n**ROLE** : `creating role...`\n**Permissions** : `setting up...`\n\n**Role permission Syncing**\n`text channel :`\n`voice channel :`\n`category :`",color=0xffffff)
            msg = await ctx.send(embed=embedcreate)

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

        embed = discord.Embed(description=f"**MUTED MEMBER**\n\n`You has been mute :` `{member.display_name}#{member.discriminator}`",color=0xffffff)
        embed.set_footer(text=f"Muted by {ctx.author}", icon_url = ctx.author.avatar.url)

        embedmute = discord.Embed(description=f"**SERVER MUTED**\n\n`You are muted on the server : {ctx.guild.name}\nReason : {reason} `\n\n",color=0xfdfd96, timestamp=datetime.now(timezone.utc))
        embedmute.set_footer(text=f"{self.client.user.name}",icon_url=self.client.user.avatar.url)

        embedfinish = discord.Embed(title="BOT SETTING SUCCESS",description=f"**ROLE** : {mutedRole.mention}\n**Permissions**\n`speak : false`\n`send message : false`\n\n**Role permission sync**\n`text channel : sync`\n`voice channel : sync`\n`category : sync`\n\n `please move` **`Muted Role`** `above other role.`",color=0xffffff)
        await ctx.send(embed = embed)
        await member.add_roles(mutedRole, reason=reason)
        await member.send(embed=embedmute)
        await msg.edit(embed = embedfinish)

    @commands.command(description="unmute member")
    @commands.has_permissions(administrator = True)
    @commands.guild_only()
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name=MUTEROLE)

        embed = discord.Embed(description=f"**UNMUTED MEMBER**\n\n`You has been unmute :` `{member.display_name}#{member.discriminator}`",color=0xffffff)
        embed.set_footer(text=f"Unmuted by {ctx.author}", icon_url = ctx.author.avatar.url)

        await member.remove_roles(mutedRole)
        await ctx.send(embed=embed)

    @commands.command(description="join voice channel")
    @commands.guild_only()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
#        await ctx.message.delete()
        await channel.connect()

    @commands.command(description="leave voice channel")
    @commands.guild_only()
    async def leave(self, ctx):
#        await ctx.message.delete()
        await ctx.voice_client.disconnect()

    @commands.command(description="lock text channel" , aliases=['lock', 'lockch'])
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
#    @commands.bot_has_guild_permissions(manage_channels=True)
    async def lock_channel(self, ctx, channel: discord.TextChannel=None):
        channel = channel or ctx.channel
        if ctx.guild.default_role not in channel.overwrites:
            embed1 = discord.Embed(description=f"{channel.name} is **lockdown.**\n\n`Note : use this cmd again for remove lockdown!`",color=0xffffff)
            overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False)
            }
            await channel.edit(overwrites=overwrites)
            await ctx.send(embed=embed1)
        elif channel.overwrites[ctx.guild.default_role].send_messages == True or channel.overwrites[ctx.guild.default_role].send_messages == None:
            embed2 = discord.Embed(description=f"{utils.emoji_converter('check')}{channel.name} is **lockdown.**\n\n`Note : use this cmd again for remove lockdown!`",color=0xffffff)
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send(embed=embed2)
        else:
            embed3 = discord.Embed(description=f"{utils.emoji_converter('check')}{channel.name} : **Removed lockdown!**",color=0xffffff)
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = True
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send(embed=embed3)

    @commands.Cog.listener()
    async def on_message(self, message):
        def _check(m):
            return (m.author == message.author
					and len(m.mentions)
					and (datetime.now(timezone.utc)-m.created_at).seconds < 60)
        
        if not message.author.bot:
            if len(list(filter(lambda m: _check(m), self.client.cached_messages))) >= 3:
                embedspam = discord.Embed(title="Spam Alert\n",description="Don't spam mentions!",color=0xffffff)
                await message.channel.send(embed=embedspam, delete_after=10)

        counter = 0
        with open("data/spam_detect.txt", "r+") as file:
            for lines in file:
                if lines.strip("\n") == str(message.author.id):
                    counter+=1

            file.writelines(f"{str(message.author.id)}\n")
            if counter > 5:
                embedmute = discord.Embed(title="Spam Alert",description=f"Mute {message.author.mention} **1 minutes**",color=0xffffff)
                member = message.author
                muter = discord.utils.get(message.guild.roles, name = MUTEROLE)     
                await member.add_roles(muter)
                await message.channel.send(embed=embedmute, delete_after=10)
                await asyncio.sleep(60)
                await member.remove_roles(muter)
            elif counter > 10:
                await message.guild.ban(message.author, reason="spam")
                await asyncio.sleep(20)
                await message.guild.unban(message.author)     


#                unmutes = await self.mute(message, [message.author], reason="Mention spam")

#                if len(unmutes):
#                    await message.channel.send("You can't use that word here.", delete_after=10)
            
#            elif message.channel.id not in self.links_allowed and search(self.url_regex, message.content):
#                await message.delete()
#                await message.channel.send("You can't send links in this channel.", delete_after=10)
            
#            elif (message.channel.id not in self.images_allowed
#			 	and any([hasattr(a, "width") for a in message.attachments])):
#                await message.delete()
#                await message.channel.send("You can't send images here.", delete_after=10)


## error commands

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embedar = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify **member** to **ban!**",color=0xffffff)
            await ctx.message.delete()
            await ctx.send(embed=embedar)
        if isinstance(error, commands.MissingPermissions):
            embedpr = discord.Embed(description=f"{utils.emoji_converter('xmark')} Only **administrators** can use this command!",color=0xffffff)
            await ctx.message.delete()
            await ctx.send(embed=embedpr) #("`You doesn't have enough permission to ban someone.`")

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embedar = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify **member** to **unban**",color=0xffffff)
            await ctx.message.delete()
            await ctx.send(embed=embedar)
        if isinstance(error, commands.MissingPermissions):
            embedpr = discord.Embed(description=f"{utils.emoji_converter('xmark')} Only **administrators** can use this command.",color=0xffffff)
            await ctx.message.delete()
            await ctx.send(embed=embedpr)
   
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embedar = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify **member** to **kick!**",color=0xffffff)
            await ctx.message.delete()
            await ctx.send(embed=embedar)
        if isinstance(error, commands.MissingPermissions):
            embedpr = discord.Embed(description=f"{utils.emoji_converter('xmark')} You doesn't have enough **permission!**",color=0xffffff)
            await ctx.message.delete()
            await ctx.send(embed=embedpr)

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embedar = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify **member** to **mute!**",color=0xffffff)
            await ctx.message.delete()
            await ctx.send(embed=embedar)
        if isinstance(error, commands.MissingPermissions):
            embedpr = discord.Embed(description=f"{utils.emoji_converter('xmark')} You doesn't have enough **permission!**",color=0xffffff)
            await ctx.message.delete()
            await ctx.send(embed=embedpr)
    
    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embedar = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify **member** to **unmute!**",color=0xffffff)
            await ctx.message.delete()
            await ctx.send(embed=embedar)
        if isinstance(error, commands.MissingPermissions):
            embedpr = discord.Embed(description=f"{utils.emoji_converter('xmark')} You doesn't have enough **permission!**",color=0xffffff)
            await ctx.message.delete()
            await ctx.send(embed=embedpr)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embedar = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify **numbers** of messages to **delete..**",color=0xffffff)
            await ctx.message.delete()
            await ctx.send(embed=embedar)
        if isinstance(error, commands.MissingPermissions):
            embedpr = discord.Embed(description=f"{utils.emoji_converter('xmark')} You doesn't have enough **permission!**",color=0xffffff)
            await ctx.message.delete()
            await ctx.send(embed=embedpr)

def setup(client):
    client.add_cog(Moderation(client))

#auto riole event
##@client.event  // auto role
##async def on_member_join(member):
##  role = get(member.guild.roles, id=role_id)
##  await member.add_roles(role)