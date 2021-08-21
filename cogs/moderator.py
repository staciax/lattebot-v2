# Standard 
import discord , datetime , asyncio , os
import json
from discord.ext import commands
from datetime import datetime, timedelta, timezone

# Third party
from re import search
from io import BytesIO
import aiohttp

# Local
import utils
from config import *

intents = discord.Intents()
intents.all()

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client        
#        self.url_regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        self.only_images = (ONLYIMG,)
#        self.images_allowed = (861874852050894868,)
        self.testing_only = (ONLYTESTING,)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
        while True:
#            print("spam detct")
            await asyncio.sleep(10)
            with open("data/spam_detect.txt", "r+") as file:
                file.truncate(0)

    @commands.command(description="ban member")
    @commands.guild_only()
#    @commands.has_permissions(administrator = True)
#    @commands.has_permissions(ban_members=True)
    @commands.has_permissions(ban_members=True)
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
    
    @commands.command(description="clear message" , aliases=['purge'])
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: str):
        if amount == 'all':
            embed = discord.Embed(
            title=f"{ctx.author.name} purged: {ctx.channel.name}",
            description=f"{amount} messages were cleared",
            color=WHITE
        )
            await ctx.channel.purge()
            await ctx.send(embed=embed, delete_after=10)
        else:
            embed = discord.Embed(
            title=f"{ctx.author.name} purged: {ctx.channel.name}",
            description=f"{amount} messages were cleared",
            color=WHITE
        )
            await ctx.channel.purge(limit=(int(amount) + 1))
            await ctx.send(embed=embed, delete_after=10)

    @commands.command(aliases=["fmute"],description="mute member")
    @commands.has_permissions(administrator = True)
    @commands.guild_only()
    async def muteforce(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(ctx.guild.roles, name=MUTEROLE)

        if not mutedRole:
            mutedRole = await guild.create_role(name=MUTEROLE , colour=discord.Colour(COLORMUTE))
            embedcreate = discord.Embed(title="BOT SETTING UP",description=f"`your server don't have` **`Muted Role`**\n`creating role...`\n**Permissions** : `setting up...`\n\n**Role permission Syncing**\n`text channel :`\n`voice channel :`\n`category :`",color=0xffffff)
            msg = await ctx.send(embed=embedcreate)

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

        embed = discord.Embed(description=f"**MUTED MEMBER**\n\n`You has been mute :` `{member.display_name}#{member.discriminator}`",color=0xffffff)
        embed.set_footer(text=f"Muted by {ctx.author}", icon_url = ctx.author.avatar.url)

        embedmute = discord.Embed(description=f"**SERVER MUTED**\n\n`You are muted on the server : {ctx.guild.name}\nReason : {reason} `\n\n",color=0xffffff, timestamp=datetime.now(timezone.utc))
        embedmute.set_footer(text=f"{self.client.user.name}",icon_url=self.client.user.avatar.url)

        embedfinish = discord.Embed(title="BOT SETTING SUCCESS",description=f"{mutedRole.mention}\n**Permissions**\n`speak : false`\n`send message : false`\n\n**Role permission sync**\n`text channel : sync`\n`voice channel : sync`\n`category : sync`\n\n `please move` **`Muted Role`** `above other role.`",color=0xffffff)
        await ctx.send(embed = embed)
        await member.add_roles(mutedRole, reason=reason)
        await member.send(embed=embedmute)
        await msg.edit(embed = embedfinish)

    @commands.command(description="mute member")
    @commands.has_permissions(administrator = True)
    @commands.guild_only()
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(ctx.guild.roles, name=MUTEROLE)

        if not mutedRole:
            embeddh = discord.Embed(title="MUTE ROLE",description=f"Your server don't have : **`Muted Role`**\n please use command : `lt muterole`",color=0xffffff)
            await ctx.send(embed=embeddh)
        else:
            embed = discord.Embed(description=f"**MUTED MEMBER**\n\n`You has been mute`: {member.name}#{member.discriminator}",color=0xffffff)
            embed.set_footer(text=f"Muted by {ctx.author}", icon_url = ctx.author.avatar.url)

            embedmute = discord.Embed(description=f"**SERVER MUTED**\n\n`You are muted on the server`: {ctx.guild.name}\n`Reason` : {reason} \n\n",color=0xffffff, timestamp=datetime.now(timezone.utc))
            embedmute.set_footer(text=f"{self.client.user.name}",icon_url=self.client.user.avatar.url)

            await ctx.send(embed = embed)
            await member.add_roles(mutedRole, reason=reason)
            await member.send(embed=embedmute)
 
    @commands.command(description="unmute member")
    @commands.has_permissions(administrator = True)
    @commands.guild_only()
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name=MUTEROLE)

        embed = discord.Embed(description=f"**UNMUTED MEMBER**\n\n`You has been unmute :` `{member.name}#{member.discriminator}`",color=0xffffff)
        embed.set_footer(text=f"Unmuted by {ctx.author}", icon_url = ctx.author.avatar.url)

        await member.remove_roles(mutedRole)
        await ctx.send(embed=embed)
    
    @commands.command(description="create mute role")
    @commands.has_permissions(administrator = True)
    @commands.guild_only()
    async def muterole(self, ctx):
        guild = ctx.guild
        mutedRole = discord.utils.get(ctx.guild.roles, name=MUTEROLE)

        if not mutedRole:
            mutedRole = await guild.create_role(name=MUTEROLE , colour=discord.Colour(COLORMUTE))
            embedmute = discord.Embed(title="CREATE MUTE ROLE",description="`creating role...`\n`please wait 10-20 seconds`",color=0xffffff)
            msg = await ctx.send(embed = embedmute)

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        
            embed = discord.Embed(title="CREATE MUTE ROLE",description=f"{mutedRole.mention}\n**Permissions**\n`speak : false`\n`send message : false`\n\n**Role permission sync**\n`text channel : sync`\n`voice channel : sync`\n`category : sync`\n\n `please move` **`Muted Role`** `above other role.`",color=0xffffff)
            await msg.edit(embed = embed)
        else:
            embedhm = discord.Embed(title="MUTE ROLE", description=f"{utils.emoji_converter('xmark')}Your server has a muted role.",color=0xffffff)
            await ctx.channel.send(embed=embedhm)

    @commands.command(description="join voice channel")
    @commands.guild_only()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
#        await ctx.message.delete()
        await channel.connect()

    @commands.command(description="leave voice channel")
    @commands.guild_only()
    async def leave_(self, ctx):
#        await ctx.message.delete()
        await ctx.voice_client.disconnect()

    @commands.command(description="lockdown or unlock text channel" , aliases=['lock', 'lockdown'])
    @commands.guild_only()
    @utils.admin_or_permissions(manage_channels=True)
#    @commands.bot_has_guild_permissions(manage_channels=True)
    async def lock_down(self, ctx, channel: discord.TextChannel=None):
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

    @commands.command(aliases=["nick"])
    @utils.admin_or_permissions(manage_nicknames=True)
    @commands.guild_only()
    async def changenick(self, ctx , member: discord.Member, nick):
        embed = discord.Embed(description=f"Nickname was changed for {member.display_name}",color=0xffffff)
        await member.edit(nick=nick)
        await ctx.channel.send(embed=embed)
    
    @commands.command(aliases=["slow"])
    @utils.admin_or_permissions(manage_channels=True)
    @commands.guild_only()
    async def slowmode(self, ctx ,*, seconds: int= None):
            if seconds == None:
                embed = discord.Embed(title="SLOW MODE",description=f"Disable slowmode this channel",color=0xffffff)
                await ctx.channel.edit(slowmode_delay=0)
                await ctx.channel.send(embed=embed)
            else:
                embed = discord.Embed(title="SLOW MODE",description=f"Set the slowmode delay in this channel to {seconds} **seconds!**",color=0xffffff)
                await ctx.channel.edit(slowmode_delay=seconds)
                await ctx.channel.send(embed=embed)

    #spam_alert
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
            
#            if (message.channel.id in self.only_images
#			 	and any([hasattr(a, "width") for a in message.attachments])):             
#                return
#            else:
#                if message.channel.id in self.only_images:
#                    em = discord.Embed(description="You can't send message in this channel.",color=PTRED2)
#                    await message.delete()
#                    await message.channel.send(embed=em , delete_after=10)
#                else:
#                    return
                                   
        counter = 0
        with open("data/spam_detect.txt", "r+") as file:
            for lines in file:
                if lines.strip("\n") == str(message.author.id):
                    counter+=1

            file.writelines(f"{str(message.author.id)}\n")
            if counter > 5:
                if not message.author.bot:
                    embedmute = discord.Embed(title="Spam Alert",description=f"Mute {message.author.mention} **1 minutes**",color=0xffffff)
                    member = message.author
                    muter = discord.utils.get(message.guild.roles, name = MUTEROLE) 
                    if not muter:
                        guild = message.guild
                        await guild.create_role(name=MUTEROLE , colour=discord.Colour(COLORMUTE))
                        for channel in guild.channels:
                            await channel.set_permissions(muter, speak=False, send_messages=False, read_message_history=True, read_messages=False)
                    await member.add_roles(muter)
                    await message.channel.send(embed=embedmute, delete_after=10)
                    await asyncio.sleep(60)
                    await member.remove_roles(muter)
                else:
                    pass
                
#            elif counter > 5:
#                await message.guild.ban(message.author, reason="spam")
#                await asyncio.sleep(20)
#                await message.guild.unban(message.author)     


#                unmutes = await self.mute(message, [message.author], reason="Mention spam")

#                if len(unmutes):
#                    await message.channel.send("You can't use that word here.", delete_after=10)
            
#            elif message.channel.id not in self.links_allowedr and seach(self.url_regex, message.content):
#                await message.delete()
#                await message.channel.send("You can't send links in this channel.", delete_after=10)
            
#            elif (message.channel.id not in self.images_allowed
#			 	and any([hasattr(a, "width") for a in message.attachments])):
#                await message.delete()
#                await message.channel.send("You can't send images here.", delete_after=10)
    
    @commands.command(aliases=["tban"])
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def tempban(self, ctx, member: utils.BetterMemberConverter, duration: utils.DurationConverter):
        multiplier = {'s': 1, 'm': 60, 'd': 86400, 'w': 604800, 'm': 2629746, 'y': 31556952 }
        amount, unit = duration
        embed = discord.Embed(title="Banned Member", description=f'{member.name} has been banned from server\n\n`Duration` : {amount}{unit}',timestamp=datetime.now(timezone.utc),color=0xffffff)
        embed.set_footer(text=f"Banned by {ctx.author}" , icon_url = ctx.author.avatar.url)
        await ctx.guild.ban(member)
        await ctx.send(embed=embed)
        await asyncio.sleep(amount * multiplier[unit])
        await ctx.guild.unban(member)

    @commands.command(aliases=["tmute"])
    @commands.guild_only()
    @commands.has_permissions(administrator = True)
#    @commands.has_permissions(manage_channels=True, manage_roles=True) 
    async def tempmute(self, ctx, member: utils.MemberConverter, duration: utils.DurationConverter):
        roles1 = discord.utils.get(ctx.guild.roles, name=MUTEROLE)
        multiplier = {'s': 1, 'm': 60, 'd': 86400, 'w': 604800, 'm': 2629746, 'y': 31556952  }
        amount, unit = duration
        guild = ctx.guild
        
        if not roles1:
            embeddh = discord.Embed(title="MUTE ROLE",description=f"Your server don't have : **`Muted Role`**\n please use command : `lt muterole`",color=RED)
            await ctx.send(embed=embeddh)
        else:
            embed = discord.Embed(description=f"**MUTED MEMBER**\n\n`You has been mute`: {member.name}#{member.discriminator}\n\n`Duration` : {amount}{unit}",color=0xffffff)
            embed.set_footer(text=f"Muted by {ctx.author}", icon_url = ctx.author.avatar.url)
            embedmute = discord.Embed(description=f"**SERVER MUTED**\n\n`You are muted on the server`: {ctx.guild.name}\n\n`Duration` : {amount}{unit} \n\n",color=0xffffff, timestamp=datetime.now(timezone.utc))
            embedmute.set_footer(text=f"{self.client.user.name}",icon_url=self.client.user.avatar.url)
            
            await member.add_roles(roles1)
            await ctx.send(embed = embed)
            await member.send(embed=embedmute)
            await asyncio.sleep(amount * multiplier[unit])
            await member.remove_roles(roles1)

#        else:
#            await ctx.guild.create_role(name=MUTEROLE)
#            role = get(ctx.guild.roles, name=MUTEROLE)
#            role1721 = discord.utils.get(ctx.guild.roles, name=MUTEROLE)
#            permissions = discord.Permissions()
#            permissions.update(add_reactions=False, send_messages=False, send_tts_messages=False, attach_files=False, connect=False)
#            await role.edit(reason = "abcd", colour = discord.Colour.red(), permissions=permissions)
#            await member.add_roles(role)
#            for channel in ctx.guild.text_channels:
#                await channel.set_permissions(role1721, add_reactions=False, send_messages=False, send_tts_messages=False, attach_files=False, connect=False)    
#        await ctx.guild.ban(member)
#        await ctx.send(f'{member} has been banned for {amount}{unit}.')
#        await asyncio.sleep(amount * multiplier[unit])
#        await ctx.guild.unban(member)
    
    @commands.command(aliases=["createei","create_emoji", "add_emoji"], description="create emoji from link")
    @commands.guild_only()
    @commands.has_permissions(manage_emojis=True)
    async def createemoji(self, ctx, url: str, *, name):
        guild = ctx.guild
        async with aiohttp.ClientSession() as ses:
            async with ses.get(url) as r:
                try:
                    img_or_gif = BytesIO(await r.read())
                    b_value = img_or_gif.getvalue()
                    if r.status in range(200, 299):
                        emoji = await guild.create_custom_emoji(image=b_value, name=name)
                        await ctx.send(f'Successfully created emoji: <:{name}:{emoji.id}>')
                        await ses.close()
                    else:
                        await ctx.send(f'Error when making request | {r.status} response.')
                        await ses.close()
                except discord.HTTPException:
                    await ctx.send('File size is too big!')

    @commands.command(aliases=["delei","delete_emoji", "del-ei"], description="delete emoji")
    @commands.guild_only()
    @commands.has_permissions(manage_emojis=True)
    async def deleteemoji(self, ctx, emoji: discord.Emoji):
        try:
            await ctx.send(f'Successfully deleted : {emoji}')
            await emoji.delete()
        except:
            await ctx.send('error delete emoji!')

    @commands.command() #testonlyme
    @utils.is_me()
    async def only_test(self, ctx):
        await ctx.send('Only you!')
        
    @commands.command()
    @commands.guild_only()
    async def roles_test(self, ctx, *, member: utils.MemberRoles):
        await ctx.send('I see the following roles: ' + ', '.join(member))

## error commands

#    @ban.error
#    async def ban_error(self, ctx, error):
#        if isinstance(error, commands.MissingRequiredArgument):
#            embedar = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify **member** to **ban!**",color=0xffffff)
#            await ctx.send(embed=embedar , delete_after=15)
#        if isinstance(error, commands.MissingPermissions):
#            embedpr = discord.Embed(description=f"{utils.emoji_converter('xmark')} Only **administrators** can use this command!",color=0xffffff)
#            await ctx.send(embed=embedpr , delete_after=15)

#    @unban.error
#    async def unban_error(self, ctx, error):
#        if isinstance(error, commands.MissingRequiredArgument):
#            embedar = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify **member** to **unban**",color=0xffffff)
#            await ctx.send(embed=embedar , delete_after=15)
#        if isinstance(error, commands.MissingPermissions):
#            embedpr = discord.Embed(description=f"{utils.emoji_converter('xmark')} Only **administrators** can use this command.",color=0xffffff)
#            await ctx.send(embed=embedpr , delete_after=15)
   
#    @kick.error
#    async def kick_error(self, ctx, error):
#        if isinstance(error, commands.MissingRequiredArgument):
#            embedar = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify **member** to **kick!**",color=0xffffff)
#            await ctx.send(embed=embedar , delete_after=15)
#        if isinstance(error, commands.MissingPermissions):
#            embedpr = discord.Embed(description=f"{utils.emoji_converter('xmark')} You doesn't have enough **permission!**",color=0xffffff)
#            await ctx.send(embed=embedpr , delete_after=15)

#    @mute.error
#    async def mute_error(self, ctx, error):
#        if isinstance(error, commands.MissingRequiredArgument):
#            embedar = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify **member** to **mute!**",color=0xffffff)
#            await ctx.send(embed=embedar , delete_after=15)
#        if isinstance(error, commands.MissingPermissions):
#            embedpr = discord.Embed(description=f"{utils.emoji_converter('xmark')} You doesn't have enough **permission!**",color=0xffffff)
#            await ctx.send(embed=embedpr , delete_after=15)
    
#    @unmute.error
#    async def unmute_error(self, ctx, error):
#        if isinstance(error, commands.MissingRequiredArgument):
#            embedar = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify **member** to **unmute!**",color=0xffffff)
#            await ctx.send(embed=embedar , delete_after=15)
#        if isinstance(error, commands.MissingPermissions):
#            embedpr = discord.Embed(description=f"{utils.emoji_converter('xmark')} You doesn't have enough **permission!**",color=0xffffff)
#            await ctx.send(embed=embedpr , delete_after=15)

#    @clear.error
#    async def clear_error(self, ctx, error):
#        if isinstance(error, commands.MissingRequiredArgument):
#            embedar = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify **numbers** of messages to **delete..**",color=0xffffff)
#            await ctx.message.delete()
#            await ctx.send(embed=embedar , delete_after=15)
#        if isinstance(error, commands.MissingPermissions):
#            embedpr = discord.Embed(description=f"{utils.emoji_converter('xmark')} You doesn't have enough **permission!**",color=0xffffff)
#            await ctx.message.delete()
#            await ctx.send(embed=embedpr , delete_after=15)
    
#    @tempban.error
#    async def tempban_error(self, ctx, error):
#        if isinstance(error, commands.MissingRequiredArgument):
#            embedar = discord.Embed(description=f"{utils.emoji_converter('xmark')} **Ban Error** | `tempban` `member` `duration`",color=0xffffff)
#            await ctx.send(embed=embedar , delete_after=15)
#        if isinstance(error, commands.MissingPermissions):
#            embedpr = discord.Embed(description=f"{utils.emoji_converter('xmark')} Only **administrators** can use this command!",color=0xffffff)
#            await ctx.send(embed=embedpr , delete_after=15)
    
#    @tempmute.error
#    async def tempmute_error(self, ctx, error):
#        if isinstance(error, commands.MissingRequiredArgument):
#            embedar = discord.Embed(description=f"{utils.emoji_converter('xmark')} **Mute Error** | `tempmute` `member` `duration`",color=0xffffff)
#            await ctx.send(embed=embedar , delete_after=15)
#        if isinstance(error, commands.MissingPermissions):
#            embedpr = discord.Embed(description=f"{utils.emoji_converter('xmark')} You doesn't have enough **permission!**",color=0xffffff)
#            await ctx.send(embed=embedpr , delete_after=15)

def setup(client):
    client.add_cog(Moderation(client))