# Standard 
import discord
import datetime
from discord.ext import commands, menus
from discord import Embed

# Third party
import aiohttp

def API_waifu_im_Embed(self, json):
    dominant_color1 = str(json['dominant_color']).replace('#', '')
    dominant_color = int(dominant_color1, 16)

    embed = Embed(title=json['tag_name'], url=json['url'], color=dominant_color) #timestamp=discord.utils.utcnow(),
    embed.set_image(url=json['url'])
    
    return embed

class sfw_all_view(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=600)
        self.ctx = ctx
        self.url = "https://api.waifu.im/sfw/all/"
        self.json_url = ""
    
    def add_button(self):
        self.add_item(discord.ui.Button(label='Image URL', url=self.json_url))
    
    async def on_timeout(self):
        self.add_button()
        await interaction.response.edit_message(view=self)
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
#        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api
                    self.json_url = json["url"]

            embed1 = API_waifu_im_Embed(self, json)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
#        if self.ctx.author.id == interaction.user.id:
            self.add_button()
            await interaction.response.edit_message(view=self)
            self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api
                self.json_url = json["url"]

        embed1 = API_waifu_im_Embed(self, json)
        
        await self.ctx.send(embed=embed1, view=self)

class sfw_waifu_view(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.url = "https://api.waifu.im/sfw/waifu/"
        self.json_url = ""
    
    def add_button(self):
        self.add_item(discord.ui.Button(label='Image URL', url=self.json_url))
    
    async def on_timeout(self):
        self.add_button()
        await interaction.response.edit_message(view=self)
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api
                    self.json_url = json["url"]

            embed1 = API_waifu_im_Embed(self, json)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        if self.ctx.author.id == interaction.user.id:
            self.add_button()
            await interaction.response.edit_message(view=self)
            self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api
                self.json_url = json["url"]

        embed1 = API_waifu_im_Embed(self, json)
        
        await self.ctx.reply(embed=embed1, view=self , mention_author=False)

class sfw_maid_view(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.url = "https://api.waifu.im/sfw/maid/"
        self.json_url = ""
    
    def add_button(self):
        self.add_item(discord.ui.Button(label='Image URL', url=self.json_url))
    
    async def on_timeout(self):
        self.add_button()
        await interaction.response.edit_message(view=self)
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api
                    self.json_url = json["url"]

            embed1 = API_waifu_im_Embed(self, json)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        if self.ctx.author.id == interaction.user.id:
            self.add_button()
            await interaction.response.edit_message(view=self)
            self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api
                self.json_url = json["url"]

        embed1 = API_waifu_im_Embed(self, json)
        
        await self.ctx.reply(embed=embed1, view=self , mention_author=False)

class nsfw_ass_view(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.url = "https://api.waifu.im/nsfw/ass/"
        self.json_url = ""
    
    def add_button(self):
        self.add_item(discord.ui.Button(label='Image URL', url=self.json_url))
    
    async def on_timeout(self):
        self.add_button()
        await interaction.response.edit_message(view=self)
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api
                    self.json_url = json["url"]

            embed1 = API_waifu_im_Embed(self, json)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        if self.ctx.author.id == interaction.user.id:
            self.add_button()
            await interaction.response.edit_message(view=self)
            self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api
                self.json_url = json["url"]

        embed1 = API_waifu_im_Embed(self, json)
        
        await self.ctx.reply(embed=embed1, view=self , mention_author=False)

class nsfw_ecchi_view(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.url = "https://api.waifu.im/nsfw/ecchi/"
        self.json_url = ""
    
    def add_button(self):
        self.add_item(discord.ui.Button(label='Image URL', url=self.json_url))
    
    async def on_timeout(self):
        self.add_button()
        await interaction.response.edit_message(view=self)
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api
                    self.json_url = json["url"]

            embed1 = API_waifu_im_Embed(self, json)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        if self.ctx.author.id == interaction.user.id:
            self.add_button()
            await interaction.response.edit_message(view=self)
            self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api
                self.json_url = json["url"]

        embed1 = API_waifu_im_Embed(self, json)
        
        await self.ctx.reply(embed=embed1, view=self , mention_author=False)

class nsfw_ero_view(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.url = "https://api.waifu.im/nsfw/ero/"
        self.json_url = ""
    
    def add_button(self):
        self.add_item(discord.ui.Button(label='Image URL', url=self.json_url))
    
    async def on_timeout(self):
        self.add_button()
        await interaction.response.edit_message(view=self)
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api
                    self.json_url = json["url"]

            embed1 = API_waifu_im_Embed(self, json)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        if self.ctx.author.id == interaction.user.id:
            self.add_button()
            await interaction.response.edit_message(view=self)
            self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api
                self.json_url = json["url"]

        embed1 = API_waifu_im_Embed(self, json)
        
        await self.ctx.reply(embed=embed1, view=self , mention_author=False)

class nsfw_hentai_view(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.url = "https://api.waifu.im/nsfw/hentai/"
        self.json_url = ""
    
    def add_button(self):
        self.add_item(discord.ui.Button(label='Image URL', url=self.json_url))
    
    async def on_timeout(self):
        self.add_button()
        await interaction.response.edit_message(view=self)
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api
                    self.json_url = json["url"]

            embed1 = API_waifu_im_Embed(self, json)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        if self.ctx.author.id == interaction.user.id:
            self.add_button()
            await interaction.response.edit_message(view=self)
            self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api
                self.json_url = json["url"]

        embed1 = API_waifu_im_Embed(self, json)
        
        await self.ctx.reply(embed=embed1, view=self , mention_author=False)

class nsfw_maid_view(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.url = "https://api.waifu.im/nsfw/maid/"
        self.json_url = ""
    
    def add_button(self):
        self.add_item(discord.ui.Button(label='Image URL', url=self.json_url))
    
    async def on_timeout(self):
        self.add_button()
        await interaction.response.edit_message(view=self)
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api
                    self.json_url = json["url"]

            embed1 = API_waifu_im_Embed(self, json)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        if self.ctx.author.id == interaction.user.id:
            self.add_button()
            await interaction.response.edit_message(view=self)
            self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api
                self.json_url = json["url"]

        embed1 = API_waifu_im_Embed(self, json)
        
        await self.ctx.reply(embed=embed1, view=self , mention_author=False)

class nsfw_milf_view(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.url = "https://api.waifu.im/nsfw/milf/"
        self.json_url = ""
    
    def add_button(self):
        self.add_item(discord.ui.Button(label='Image URL', url=self.json_url))
    
    async def on_timeout(self):
        self.add_button()
        await interaction.response.edit_message(view=self)
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api
                    self.json_url = json["url"]

            embed1 = API_waifu_im_Embed(self, json)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        if self.ctx.author.id == interaction.user.id:
            self.add_button()
            await interaction.response.edit_message(view=self)
            self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api
                self.json_url = json["url"]

        embed1 = API_waifu_im_Embed(self, json)
        
        await self.ctx.reply(embed=embed1, view=self , mention_author=False)

class nsfw_oppai_view(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.url = "https://api.waifu.im/nsfw/oppai/"
        self.json_url = ""
    
    def add_button(self):
        self.add_item(discord.ui.Button(label='Image URL', url=self.json_url))
    
    async def on_timeout(self):
        self.add_button()
        await interaction.response.edit_message(view=self)
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api
                    self.json_url = json["url"]

            embed1 = API_waifu_im_Embed(self, json)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        if self.ctx.author.id == interaction.user.id:
            self.add_button()
            await interaction.response.edit_message(view=self)
            self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api
                self.json_url = json["url"]

        embed1 = API_waifu_im_Embed(self, json)
        
        await self.ctx.reply(embed=embed1, view=self , mention_author=False)

class nsfw_oral_view(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.url = "https://api.waifu.im/nsfw/oral/"
        self.json_url = ""
    
    def add_button(self):
        self.add_item(discord.ui.Button(label='Image URL', url=self.json_url))
    
    async def on_timeout(self):
        self.add_button()
        await interaction.response.edit_message(view=self)
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api
                    self.json_url = json["url"]

            embed1 = API_waifu_im_Embed(self, json)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        if self.ctx.author.id == interaction.user.id:
            self.add_button()
            await interaction.response.edit_message(view=self)
            self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api
                self.json_url = json["url"]

        embed1 = API_waifu_im_Embed(self, json)
        
        await self.ctx.reply(embed=embed1, view=self , mention_author=False)

class nsfw_paizuri_view(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.url = "https://api.waifu.im/nsfw/paizuri/"
        self.json_url = ""
    
    def add_button(self):
        self.add_item(discord.ui.Button(label='Image URL', url=self.json_url))
    
    async def on_timeout(self):
        self.add_button()
        await interaction.response.edit_message(view=self)
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api
                    self.json_url = json["url"]

            embed1 = API_waifu_im_Embed(self, json)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        if self.ctx.author.id == interaction.user.id:
            self.add_button()
            await interaction.response.edit_message(view=self)
            self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api
                self.json_url = json["url"]

        embed1 = API_waifu_im_Embed(self, json)
        
        await self.ctx.reply(embed=embed1, view=self , mention_author=False)

class nsfw_selfies_view(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.url = "https://api.waifu.im/nsfw/selfies/"
        self.json_url = ""
    
    def add_button(self):
        self.add_item(discord.ui.Button(label='Image URL', url=self.json_url))
    
    async def on_timeout(self):
        self.add_button()
        await interaction.response.edit_message(view=self)
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api
                    self.json_url = json["url"]

            embed1 = API_waifu_im_Embed(self, json)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        if self.ctx.author.id == interaction.user.id:
            self.add_button()
            await interaction.response.edit_message(view=self)
            self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api
                self.json_url = json["url"]

        embed1 = API_waifu_im_Embed(self, json)
        
        await self.ctx.reply(embed=embed1, view=self , mention_author=False)

class nsfw_uniform_view(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.url = "https://api.waifu.im/nsfw/uniform/"
        self.json_url = ""
    
    def add_button(self):
        self.add_item(discord.ui.Button(label='Image URL', url=self.json_url))
    
    async def on_timeout(self):
        self.add_button()
        await interaction.response.edit_message(view=self)
        self.stop()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.ctx.author.id == interaction.user.id:
            async with aiohttp.ClientSession() as session:
                request = await session.get(self.url)
                api = await request.json()
                if request.status == 200:
                    json = api
                    self.json_url = json["url"]

            embed1 = API_waifu_im_Embed(self, json)
                
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        if self.ctx.author.id == interaction.user.id:
            self.add_button()
            await interaction.response.edit_message(view=self)
            self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(self.url)
            api = await request.json()
            if request.status == 200:
                json = api
                self.json_url = json["url"]

        embed1 = API_waifu_im_Embed(self, json)
        
        await self.ctx.reply(embed=embed1, view=self , mention_author=False)

