# Standard 
import discord , datetime , time , os
from discord.ext import commands , tasks
from datetime import datetime, timezone
from discord.channel import TextChannel
from asyncio import sleep

# Third party
# Local
from config import *
import utils
from utils import create_voice_channel , get_channel_by_name

intents = discord.Intents()
intents.all()

private_channel = PRIVATE_LOGS #chat #nsfw #onlyfans #underworld #

class Activities(commands.Cog):

    current_streamers = list()

    def __init__(self, client):
        self.bot = client
        self.client = client
        self.invites = {}
        self.total_ = 0
        self.member_ = 0
        self.bot_ = 0
        self.role_ = 0
        self.channel_ = 0
        self.text_ = 0
        self.voice_ = 0
        self.boost_ = 0
        self.counted.start()
    
    def cog_unload(self):
        self.counted.cancel()

    @tasks.loop(minutes=30)
    async def counted(self):
        guild = self.bot.get_guild(840379510704046151)

        total_count = guild.member_count
        if self.total_ != total_count:
            self.total_ = total_count
            total_channel = guild.get_channel(876738880282431489)
            total_name = f"ᴛᴏᴛᴀʟ‌・{self.total_}"
            print(total_name)
            await total_channel.edit(name=total_name)
        
        member_count = len([member for member in guild.members if not member.bot])
        if self.member_ != member_count:
            self.member_ = member_count
            member_channel = guild.get_channel(876712142160678923)
            member_name = f"ᴍᴇᴍʙᴇʀs・{self.member_}"
            print(member_name)
            await member_channel.edit(name=member_name)

        bot_count = len([Member for Member in guild.members if Member.bot])
        if self.bot_ != bot_count:
            self.bot_ = bot_count
            bot_channel = guild.get_channel(876724022686150687)
            bot_name = f"ʙᴏᴛs‌・{self.bot_}"
            print(bot_name)
            await bot_channel.edit(name=bot_name)
        
        role_count = len(guild.roles)
        if self.role_ != role_count:
            self.role_ = role_count
            role_channel = guild.get_channel(876712169662742588)
            role_name = f"ʀᴏʟᴇs‌・{self.role_}"
            print(role_name)
            await role_channel.edit(name=role_name)
        
        channel_count = len(guild.channels)
        if self.channel_ != channel_count:
            self.channel_ = channel_count
            channel_channel = guild.get_channel(876712200214024192)
            channel_name = f"ᴄʜᴀɴɴᴇʟs・{self.channel_}"
            print(channel_name)
            await channel_channel.edit(name=channel_name)
        
        text_channel_count = len(guild.text_channels)
        if self.text_ != text_channel_count:
            self.text_ = text_channel_count
            text_channel = guild.get_channel(876740437505871922)
            text_name = f"ᴛᴇxᴛ・{self.text_}"
            print(text_name)
            await text_channel.edit(name=text_name)
        
        voice_channel_count = len(guild.voice_channels)
        if self.voice_ != voice_channel_count:
            self.voice_ = voice_channel_count
            voice_channel = guild.get_channel(876740515863879711)
            voice_name = f"ᴠᴏɪᴄᴇ・{self.voice_}"
            print(voice_name)
            await voice_channel.edit(name=voice_name)
        
        boost_count = guild.premium_subscription_count
        if self.boost_ != boost_count:
            self.boost_ = boost_count
            boost_channel = guild.get_channel(876737270051389470)
            boost_name = f"ʙᴏᴏꜱᴛꜱ・{self.boost_}"
            print(boost_name)
            await boost_channel.edit(name=boost_name)

    @counted.before_loop
    async def before_counted(self):
        await self.bot.wait_until_ready()

#    @commands.Cog.listener()
#    async def on_member_join(self, member):
#        if member.guild.id == 867729118308204564:
#	        await sleep(60*10)
#	        for channel in member.guild.channels:
#		        if channel.name.startswith('♢・latte'):
#			        await channel.edit(name=f'♢・latte・{member.guild.member_count}')
#			        break
#auto riole event
#@commands.Cog.listener()
#async def on_member_join(self, member):
##  role = get(member.guild.roles, id=role_id)
##  await member.add_roles(role)

    @commands.Cog.listener()
    async def on_ready(self):
        self.log_welcome = self.bot.get_channel(WELCOME_LOG)
        self.log_leave = self.bot.get_channel(lEAVE_LOG)
        self.log_channel = self.bot.get_channel(SERVER_LOG)
        self.log_voice = self.bot.get_channel(VOICE_LOG)
        self.log_message = self.bot.get_channel(MESSAGE_LOG)
        self.log_roles = self.bot.get_channel(ROLES_LOG)
        print(f"-{self.__class__.__name__}")
        for guild in self.client.guilds:
            self.invites[guild.id] = await guild.invites()
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == MYGUILD: #only my guild
            """welcome log"""
            invites_before_join = self.invites[member.guild.id]
            invites_after_join = await member.guild.invites()
            for invite in invites_before_join:
                if invite.uses < utils.find_invite_by_code(invites_after_join, invite.code).uses:
                    embed2 = discord.Embed(
                        title="Member join",
                        color=PTGREEN,
                        timestamp=datetime.now(timezone.utc)
                    )
                    embed2.add_field(name="Name:", value=f"{member.name}", inline=False)
                    embed2.add_field(name="Invite Code:", value=f"||{invite.code}||", inline=False)
                    embed2.set_thumbnail(url=member.avatar.url)
                    embed2.set_footer(text=f"Invited by {invite.inviter.name}", icon_url=invite.inviter.avatar.url)
                    await self.log_channel.send(embed=embed2)
                    self.invites[member.guild.id] = invites_after_join
#                    return     

            """welcome embed"""
        
            embed=discord.Embed(
                            description=f"ʚ˚̩̥̩ɞ ◟‧Welcome‧ *to* **{member.guild}!** <a:ab__purplestar:854958903656710144>\n　。\nෆ ₊˚don’t forget to check out . . .\n\n♡ ꒷ get latte roles~︰𓂃 ꒱\n⸝⸝﹒<#861774918290636800> \n⸝⸝﹒<#840380566862823425>\n\n⸝⸝﹒||{member.mention}|| ꒱ {utils.emoji_converter('3rd')}", #⊹₊˚**‧Welcome‧**˚₊⊹ 
                            timestamp=datetime.now(timezone.utc),
                            color=0xc4cfcf
    
                )
            embed.set_author(name=f"{member}", icon_url=member.avatar.url), 
            embed.set_thumbnail(url=member.avatar.url)
            embed.set_footer(text=f"You're our {member.guild.member_count} members ෆ"),

            await self.log_welcome.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_member_ban(self, guild, member):
        if member.guild.id == MYGUILD:
            embed = discord.Embed(
                description=f"**Member ban\n`{member}`**",
                color=PTRED)
            embed.set_thumbnail(url=member.avatar.url)
            embed.set_footer(text="—・good bye bro")
            embed.timestamp = datetime.now(timezone.utc)

            await self.log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id == MYGUILD: #only my guild
            embed3 = discord.Embed(
                        title="Member leave",
                        color=PTRED2,
                        timestamp=datetime.now(timezone.utc)
                    )
            embed3.add_field(name="Name:", value=f"{member.name}#{member.discriminator}", inline=False)
            embed3.set_thumbnail(url=member.avatar.url)
#           embed3.set_footer(text=member.guild, icon_url=member.guild.icon.url)
            await self.log_channel.send(embed=embed3)
            self.invites[member.guild.id] = await member.guild.invites()

            """leave embed"""

            embed = discord.Embed(
                        description=f"**Leave Server\n`{member}`**",
                        color=0xdbd7d2)
            embed.set_thumbnail(url=member.avatar.url)
            embed.set_footer(text="—・see ya good bye")
            embed.timestamp = datetime.now(timezone.utc)

            await self.log_leave.send(embed = embed) #await channel.send(f"{member} has left the server")
    
    @commands.Cog.listener()
    async def on_invite_create(self, invite: discord.Invite):
        if invite.guild.id == MYGUILD:
            now = datetime.now(timezone.utc)
            max_use_count = "Unlimited" if invite.max_uses == 0 else invite.max_uses
            embed = discord.Embed(title=f"{invite.inviter} created an invite.", timestamp=now, colour=WHITE)
            embed.add_field(name="Max Uses:", value=f"{max_use_count}")
            embed.add_field(name="Channel:", value=f"#{invite.channel}")
            embed.add_field(name="Inivte Code:", value=f"||{invite.code}||")
            embed.set_footer(text = f'Created by {invite.inviter.name}', icon_url =invite.inviter.avatar.url)
            await self.log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_user_update(self, before, after):
            if before.name != after.name:
                embed = discord.Embed(title="Username change",colour=after.colour,timestamp=datetime.now(timezone.utc))

                fields = [("**Before**", f"```{before.name}```", False),
					    ("**After**", f"```{after.name}```", False)]

                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)
                    embed.set_thumbnail(url=after.avatar.url)
                    embed.set_footer(text=f"{after.display_name}", icon_url=after.avatar.url)
            
                await self.log_channel.send(embed=embed)

            if before.discriminator != after.discriminator:
                embed = discord.Embed(title="Discriminator change",
                                    colour=0xffffff, #after.colour
                                    timestamp=datetime.now(timezone.utc))

                fields = [("**Before**",f"```#{before.discriminator}```", False),
					    ("**After**",f"```#{after.discriminator}```", False)]
            
                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)
                    embed.set_footer(text=f"{after.display_name}", icon_url=after.avatar.url)
            
                await self.log_channel.send(embed=embed)
        
            if before.avatar.url != after.avatar.url:
                embed = discord.Embed(title="Avatar change",description="New image is below, old to the right.",
						    colour=0xf3d4b4,
						    timestamp=datetime.now(timezone.utc))
                embed.set_thumbnail(url=before.avatar.url)
                embed.set_image(url=after.avatar.url)
                embed.set_footer(text=f"{after.display_name}", icon_url=after.avatar.url)

                await self.log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.guild.id == MYGUILD:
            if before.display_name != after.display_name:
                embed = discord.Embed(title="Nickname change",
                                    colour=0xFFDF00, #colour=after.colour,
						            timestamp=datetime.now(timezone.utc))

                fields = [("**Before**", f"```{before.display_name}```", False),
					    ("**After**", f"```{after.display_name}```", False)]

                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)
                    embed.set_thumbnail(url=after.avatar.url)
                    embed.set_footer(text="", icon_url=after.avatar.url)

                await self.log_channel.send(embed=embed)
        
            elif before.roles != after.roles:
                new_roles = [x.mention for x in after.roles if x not in before.roles]
                old_roles = [x.mention for x in before.roles if x not in after.roles]
                if new_roles:
                    name = "**Add role**"
                    nr_str = str(new_roles)[2:-2]
                    nr_valur = ", ".join([r.mention for r in after.roles])
                    color = 0x52D452
                else:
                    name = "**Remove role**"
                    nr_str = str(old_roles)[2:-2]
                    nr_valur = ", ".join([r.mention for r in after.roles])
                    color = 0xFF6961
                offline = ['<@&873693874198052876>']
                if new_roles == offline:
                    return
                if old_roles == offline:
                    return
                embed = discord.Embed(colour=color, #colour=after.colour,
						            timestamp=datetime.now(timezone.utc))
                
                embed.set_author(name=f"{after.display_name} | Role updates", icon_url=after.avatar.url)

                fields = [("**Current role**", nr_valur , False),
					        (name , nr_str , False)]

                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)

                await self.log_roles.send(embed=embed)
            else:
                return

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if not before.channel.id in private_channel:
            if not after.author.bot:
                if before.content != after.content:
                    embed = discord.Embed(description=f"**Edited in**: {after.channel.mention}\n**Message link:** ||[click]({after.jump_url})||",
                                colour=0xFF8C00, #after.author.colour,
                                timestamp=datetime.now(timezone.utc))
                    embed.set_author(name=after.author.display_name , url=after.jump_url ,icon_url=after.author.avatar.url)
                    embed.set_footer(text="Message edit")
                
                    fields = [("**Before**", f"```{before.content}```" , False),
						    ("**After**", f"```{after.content}```", False)]
                
                    for name, value, inline in fields:
                        embed.add_field(name=name, value=value, inline=inline)
                
                    await self.log_message.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if not message.channel.id in private_channel:
            if message.guild: #if message.guild.id:
                if not message.author.bot:
                    channel = self.bot.get_channel(MESSAGE_LOG)

                    em = discord.Embed(color=0xDC143C , timestamp=datetime.now(timezone.utc))
                    em.set_author(name=message.author.display_name, url=message.jump_url ,icon_url=message.author.avatar.url)

                    if message.attachments is not None:
                        if len(message.attachments) > 1:
                            im = [x.proxy_url for x in message.attachments]
                            em.add_field(name='\uFEFF',value = f"This Message Contained {len(message.attachments)} Message Attachments, Please See Below")
                            await channel.send(' '.join(im))
                        elif message.attachments:
                            image = message.attachments[0].proxy_url
                            em.description = f"**Deleted in:** {message.channel.mention}"
                            em.set_image(url=image)
                            em.set_footer(text="Message delete")
                        else:
                            em.description = f"**Deleted in:** {message.channel.mention}"
                            em.add_field(name=f"**Content:**", value=f"```{message.clean_content}```", inline=False)
                            em.set_footer(text="Message delete")

                    await self.log_message.send(embed=em)
                else:
                    pass
            else:
                delem = discord.Embed(color=0xDC143C , timestamp=datetime.now(timezone.utc))
                delem.set_author(name=message.author.display_name,icon_url=message.author.avatar.url)
                delem.description = f"**Message deleted in:** {message.channel}"
                delem.add_field(name=f"**Content:**", value=f"```{message.clean_content}```", inline=False)
                delem.set_footer(text="Message delete")

                await self.log_channel.send(embed=delem)
    
    @commands.Cog.listener()
    async def on_voice_state_update(self , member, before, after):
        if member.guild.id == MYGUILD:
            embed = discord.Embed(description="",timestamp=datetime.now(timezone.utc))
            if member.bot:
                return
        
            if not before.channel:
                embed.description += f"**JOIN CHANNEL** : `{after.channel.name}`"
                embed.set_footer(text=f"{member.name}#{member.discriminator}" , icon_url=member.avatar.url)
                embed.color=PTGREEN
                await self.log_voice.send(embed=embed)
        
            if before.channel and not after.channel:
                embed.description += f"**LEFT CHANNEL** : `{before.channel.name}`"
                embed.set_footer(text=f"{member.name}#{member.discriminator}" , icon_url=member.avatar.url)
                embed.color=PTRED2
                await self.log_voice.send(embed=embed)
        
            if before.channel and after.channel:
                if before.channel.id != after.channel.id:
                    embed.description += f"**SWITCHED CHANNELS** : `{before.channel.name}` to `{after.channel.name}`"
                    embed.set_footer(text=f"{member.name}#{member.discriminator}" , icon_url=member.avatar.url)
                    embed.color=PTYELLOW2
                    await self.log_voice.send(embed=embed)
                else:
                    if member.voice.self_stream:
                        embedstm = discord.Embed(description=f"**STREAMING in** : `{before.channel.name}`",timestamp=datetime.now(timezone.utc))
                        embedstm.set_footer(text=f"{member.name}#{member.discriminator}" , icon_url=member.avatar.url)
                        embedstm.colour=PURPLE
                        self.current_streamers.append(member.id)
                        await self.log_voice.send(embed=embedstm)

                    elif member.voice.mute:
                        embedmute = discord.Embed(description=f"**SERVER MUTED** in `{after.channel.name}`")
                        embedmute.set_footer(text=f"{member.name}#{member.discriminator}" , icon_url=member.avatar.url)
                        embedmute.colour=PTRED
                        await self.log_voice.send(embed=embedmute)

                    elif member.voice.deaf:
                        embeddeaf = discord.Embed(description=f"**SERVER DEAFEN** in `{after.channel.name}`")
                        embeddeaf.set_footer(text=f"{member.name}#{member.discriminator}" , icon_url=member.avatar.url)
                        embeddeaf.colour=PTRED
                        await self.log_voice.send(embed=embeddeaf)

                    else:
                        if member.voice.deaf:
                            print("unmuted")
                        for streamer in self.current_streamers:
                            if member.id == streamer:
                                if not member.voice.self_stream:
                                    print("user stopped streaming")
                                    self.current_streamers.remove(member.id)
                                break        
        else:
            return

        if after.channel is not None:
            if after.channel.name == "・ᵁᴺᴰᴱᴿᵂᴼᴿᴸᴰ・":
                chname = "ᵁᴺᴰᴱᴿᵂᴼᴿᴸᴰ"
                checkvoice = get_channel_by_name(after.channel.guild, channel_name=chname)
                if checkvoice is None:
                    channel = await create_voice_channel(after.channel.guild, f'{chname}'.lower() , category_name="୨ ♡ ─ 「 Private 」♡")
                    
                    if channel is not None:
                        await member.move_to(channel)
                    
                elif checkvoice:
                    await member.move_to(checkvoice)
                else:
                    return
                    
            if after.channel.name == "・ᴹᴼᴼᴺᴸᴵᴳᴴᵀ・":
                chname = "ᴹᴼᴼᴺᴸᴵᴳᴴᵀ"
                checkvoice = get_channel_by_name(after.channel.guild, channel_name=chname)
                if checkvoice is None:
                    channel = await create_voice_channel(after.channel.guild, f'{chname}'.lower() , category_name="୨ ♡ ─ 「 Private 」♡")
                    
                    if channel is not None:
                        await member.move_to(channel)
                    
                elif checkvoice:
                    await member.move_to(checkvoice)
                else:
                    return
                
#    @commands.Cog.listener() #activity = role
#    async def on_presence_update(self, before, after):
#        games = ["game1", "game2", "game3"]
#        if after.activity and after.activity.name.lower() in games:
#            role = discord.utils.get(after.guild.roles, name=after.activity)
#            await after.add_roles(role)
#        elif before.activity and before.activity.name.lower() in games and not after.activity:
#            role = discord.utils.get(after.guild.roles, name=after.activity)
#            if role in after.roles: 
#                await after.remove_roles(role)

    @commands.Cog.listener() #online offlie = role
    async def on_presence_update(self, before, after):
        guild = self.bot.get_guild(840379510704046151)
        role = discord.utils.find(lambda r: r.name == '୨ offline ୧', guild.roles)
        if before.guild.id == MYGUILD:
            if str(after.status) == "online" or "dnd" and "idle":
                await before.remove_roles(role)
            if str(after.status) == "offline":
                await after.add_roles(role)
            else:
                return
        
def setup(client):
    client.add_cog(Activities(client))