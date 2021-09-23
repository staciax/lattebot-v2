# Standard 
import discord
import datetime
from discord.ext import commands, menus
from discord import Embed

# Third party
import aiohttp

def API_waifu_im_Embed(self, json, title):
    embed = discord.Embed(title=title,url=json["url"], color=0xffffff)
    embed.set_image(url=json['url'])
 
    return embed

class sfw_waifu(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Waifu"
        self.url = "https://api.waifu.pics/sfw/waifu"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_neko(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Neko"
        self.url = "https://api.waifu.pics/sfw/neko"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_shinobu(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Shinobu"
        self.url = "https://api.waifu.pics/sfw/shinobu"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_megumin(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Megumin"
        self.url = "https://api.waifu.pics/sfw/megumin"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_bully(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Bully"
        self.url = "https://api.waifu.pics/sfw/bully"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_cuddle(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Cuddle"
        self.url = "https://api.waifu.pics/sfw/cuddle"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_cry(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Cry"
        self.url = "https://api.waifu.pics/sfw/cry"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_hug(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Hug"
        self.url = "https://api.waifu.pics/sfw/hug"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_awoo(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Awoo"
        self.url = "https://api.waifu.pics/sfw/awoo"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_kiss(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Kiss"
        self.url = "https://api.waifu.pics/sfw/kiss"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_lick(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Lick"
        self.url = "https://api.waifu.pics/sfw/lick"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_pat(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Pat"
        self.url = "https://api.waifu.pics/sfw/pat"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_hug(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Hug"
        self.url = "https://api.waifu.pics/sfw/hug"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_smug(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Smug"
        self.url = "https://api.waifu.pics/sfw/smug"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_bonk(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Bonk"
        self.url = "https://api.waifu.pics/sfw/bonk"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_yeet(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Yeet"
        self.url = "https://api.waifu.pics/sfw/yeet"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_blush(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Blush"
        self.url = "https://api.waifu.pics/sfw/blush"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_smile(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Smile"
        self.url = "https://api.waifu.pics/sfw/smile"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_wave(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Wave"
        self.url = "https://api.waifu.pics/sfw/wave"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_highfive(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Hug"
        self.url = "https://api.waifu.pics/sfw/highfive"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_handhold(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Handhold"
        self.url = "https://api.waifu.pics/sfw/handhold"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_nom(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Nom"
        self.url = "https://api.waifu.pics/sfw/nom"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_bite(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Bite"
        self.url = "https://api.waifu.pics/sfw/bite"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_glomp(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Glomp"
        self.url = "https://api.waifu.pics/sfw/glomp"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_slap(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Slap"
        self.url = "https://api.waifu.pics/sfw/slap"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_kill(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Kill"
        self.url = "https://api.waifu.pics/sfw/kill"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_kick(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Kick"
        self.url = "https://api.waifu.pics/sfw/kick"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_happy(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Happy"
        self.url = "https://api.waifu.pics/sfw/happy"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_wink(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Wink"
        self.url = "https://api.waifu.pics/sfw/wink"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_poke(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Poke"
        self.url = "https://api.waifu.pics/sfw/poke"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_dance(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Dance"
        self.url = "https://api.waifu.pics/sfw/dance"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class sfw_cringe(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Cringe"
        self.url = "https://api.waifu.pics/sfw/cringe"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class nsfw_waifu(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Waifu"
        self.url = "https://api.waifu.pics/nsfw/waifu"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class nsfw_neko(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Neko"
        self.url = "https://api.waifu.pics/nsfw/neko"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class nsfw_trap(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Trap"
        self.url = "https://api.waifu.pics/nsfw/trap"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class nsfw_blowjob(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = "Blowjob"
        self.url = "https://api.waifu.pics/nsfw/blowjob"
    
    async def on_timeout(self):
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api

        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)