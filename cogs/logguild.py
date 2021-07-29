# Standard 
import discord
import datetime
import time
from discord.ext import commands
from datetime import datetime, timezone

# Third party
# Local
from config import *
from utils import create_voice_channel , get_channel_by_name

private_channel = PRIVATE_LOGS #chat #nsfw #onlyfans #underworld

class Logguild(commands.Cog):

    current_streamers = list()

    def __init__(self, client):
        self.bot = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.log_channel = self.bot.get_channel(SERVER_LOG)
        self.log2_channel = self.bot.get_channel(EMOJISERVER_LOG)
        print(f"-{self.__class__.__name__}")

    @commands.Cog.listener()
    async def on_user_update(self, before, after):
            if before.name != after.name:
                embed = discord.Embed(title="Username change",colour=after.colour,timestamp=datetime.utcnow())

                fields = [("`Before`", before.name, False),
					    ("`After`", after.name, False)]

                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)
                    embed.set_thumbnail(url=after.avatar.url)
                    embed.set_footer(text=f"{after.display_name}", icon_url=after.avatar.url)
            
                await self.log_channel.send(embed=embed)
                await self.log2_channel.send(embed=embed)


            if before.discriminator != after.discriminator:
                embed = discord.Embed(title="Discriminator change",
                                    colour=0xffffff, #after.colour
                                    timestamp=datetime.utcnow())

                fields = [("`Before`",f"#{before.discriminator}", False),
					    ("`After`",f"#{after.discriminator}", False)]
            
                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)
                    embed.set_footer(text=f"{after.display_name}", icon_url=after.avatar.url)
            
                await self.log_channel.send(embed=embed)
                await self.log2_channel.send(embed=embed)
        

            if before.avatar.url != after.avatar.url:
                embed = discord.Embed(title="Avatar change",description="New image is below, old to the right.",
						    colour=self.log_channel.guild.get_member(after.id).colour,
						    timestamp=datetime.utcnow())
                embed.set_thumbnail(url=before.avatar.url)
                embed.set_image(url=after.avatar.url)
                embed.set_footer(text=f"{after.display_name}", icon_url=after.avatar.url)

                await self.log_channel.send(embed=embed)
                await self.log2_channel.send(embed=embed)

    
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.guild.id == MYGUILD:
            if before.display_name != after.display_name:
                embed = discord.Embed(title="Nickname change",
                                    colour=0xFFDF00, #colour=after.colour,
						            timestamp=datetime.utcnow())

                fields = [("`Before`", before.display_name, False),
					    ("`After`", after.display_name, False)]

                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)
                    embed.set_thumbnail(url=after.avatar.url)
                    embed.set_footer(text="", icon_url=after.avatar.url)

                await self.log_channel.send(embed=embed)
                await self.log2_channel.send(embed=embed)
        

            elif before.roles != after.roles:
                embed = discord.Embed(title="Role updates",
                                    colour=0xb19cd9, #colour=after.colour,
						            timestamp=datetime.utcnow())

                fields = [(" `Before`", ", ".join([r.mention for r in before.roles]), False),
					    ("`After`", ", ".join([r.mention for r in after.roles]), False)]

                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)
                    embed.set_footer(text=f"{after.display_name}", icon_url=after.avatar.url)

                await self.log_channel.send(embed=embed)
                await self.log2_channel.send(embed=embed)
        else:
            pass

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if not before.channel.id in private_channel:
            if not after.author.bot:
                if before.content != after.content:
                    embed = discord.Embed(title="Message edit",
                                colour=0xFF8C00, #after.author.colour,
                                timestamp=datetime.utcnow())
                
                    fields = [("`Before`", before.content , False),
						    ("`After`", after.content, False)]
                
                    for name, value, inline in fields:
                        embed.add_field(name=name, value=value, inline=inline)
                        embed.set_footer(text=f"{after.author.display_name}", icon_url=after.author.avatar.url)
                
                    await self.log_channel.send(embed=embed)
                    await self.log2_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if not message.channel.id in private_channel:
            if message.guild: #if message.guild.id:
                if not message.author.bot:
                    channel = self.bot.get_channel(SERVER_LOG)

                    em = discord.Embed(color=0xDC143C,title = f"Message Deleted:")
                    em.set_footer(text=self.bot.user.name,icon_url=self.bot.user.avatar.url )
                    em.set_author(name=message.author.display_name,icon_url=message.author.avatar.url)

                    if message.attachments is not None:
                        if len(message.attachments) > 1:
                            im = [x.proxy_url for x in message.attachments]
                            em.add_field(name='\uFEFF',value = f"This Message Contained {len(message.attachments)} Message Attachments, Please See Below")
                            await channel.send(' '.join(im))
                        elif message.attachments:
                            image = message.attachments[0].proxy_url
                            em.description = f"**Deleted in:** {message.channel.mention}"
                            em.set_image(url=image)
                        else:
                            em.description = f"**Deleted in:** {message.channel.mention} \n**Content:** {message.clean_content}"



                    await self.log_channel.send(embed=em)
                    await self.log2_channel.send(embed=em)
                else:
                    pass
            else:
                delem = discord.Embed(color=0xDC143C,title = f"Message Deleted:")
                delem.set_footer(text=self.bot.user.name,icon_url=self.bot.user.avatar.url )
                delem.set_author(name=message.author.display_name,icon_url=message.author.avatar.url)
                delem.description = f"**Deleted in:** {message.channel} \n**Content:** {message.clean_content}"

                await self.log_channel.send(embed=delem)
                await self.log2_channel.send(embed=delem)
    
    @commands.Cog.listener()
    async def on_voice_state_update(self , member, before, after):
        embed = discord.Embed(description="",timestamp=datetime.utcnow(),color=WHITE)
        if member.bot:
            return
        
        if not before.channel:
            embed.description += f"**join channel** : `{after.channel.name}`"
            embed.set_footer(text=f"{member.name}#{member.discriminator}" , icon_url=member.avatar.url)
            await self.log_channel.send(embed=embed)
#            print(f'{member.name} Join {after.channel.name}') 
        
        if before.channel and not after.channel:
            embed.description += f"**left channel** : `{before.channel.name}`"
            embed.set_footer(text=f"{member.name}#{member.discriminator}" , icon_url=member.avatar.url)
#            print(f"{member.name} left channel {before.channel.name}")
            await self.log_channel.send(embed=embed)
        
        if before.channel and after.channel:
            if before.channel.id != after.channel.id:
                embed.description += f"**switched channels** : `{before.channel.name}` to `{after.channel.name}`"
                embed.set_footer(text=f"{member.name}#{member.discriminator}" , icon_url=member.avatar.url)
                await self.log_channel.send(embed=embed)
#                print("user switched voice channels")
            else:
                print("something else happend!")
                if member.voice.self_stream:
                    embed.description += f"**started streaming in** : `{before.channel.name}`"
                    embed.set_footer(text=f"{member.name}#{member.discriminator}" , icon_url=member.avatar.url)
#                    print("user started streaming")
                    self.current_streamers.append(member.id)
                    await self.log_channel.send(embed=embed)
                elif member.voice.self_mute:
                    print("User muted")
                elif member.voice.self_deaf:
                    print("user deafened")
                elif member.voice.mute:
                    print(f"{member.name} User muted")
                elif member.voice.deaf:
                    print("guild user deafened")
                elif member.self_video:
                    print("member live stream")
                else:
                    print("we are here")
                    for streamer in self.current_streamers:
                        if member.id == streamer:
                            if not member.voice.self_stream:
                                print("user stopped streaming")
                                self.current_streamers.remove(member.id)
                            break
        
#        if after.channel is not None:
#            if after.channel.name == "✧・Game":
#                chname = '♢'
#                checkvoice = get_channel_by_name(after.channel.guild, channel_name=chname)
#                if checkvoice is None:
#                    channel = await create_voice_channel(after.channel.guild, f'{chname}'.lower() , category_name="୨ ♡ ─ 「 Admin Only 」♡")
#                    
#                    if channel is not None:
#                        await member.move_to(channel)
#                    
#                else:
#                    await member.move_to(checkvoice)
        
            
            
        

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

#    @commands.Cog.listener() #online offlie = role
#    async def on_presence_update(self, before, after):
#        if str(before.status) == "online":
#            if str(after.status) == "offline":
#                guild = self.bot.get_guild(840379510704046151)
#                role = discord.utils.find(lambda r: r.name == '୨ offline role ୧', guild.roles)
#                await after.add_roles(role)
#                await before.remove_roles(role)


def setup(client):
    client.add_cog(Logguild(client))