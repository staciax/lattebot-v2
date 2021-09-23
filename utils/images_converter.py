# Standard 
import discord , json
import datetime
from discord.ext import commands, menus

# Third party
import aiohttp

class cat_view(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.url = "http://aws.random.cat/meow"
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
            async with aiohttp.ClientSession() as cs:
                async with cs.get(self.url) as r:
                    data = await r.json()
                    self.json_url = data['file']

                    embed = discord.Embed(title="Meow" , color=0xffffff)
                    embed.set_image(url=data['file'])

        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        if self.ctx.author.id == interaction.user.id:
            self.add_button()
            await interaction.response.edit_message(view=self)
            self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.url) as r:
                data = await r.json()
                self.json_url = data['file']

                embed = discord.Embed(title="Meow" , color=0xffffff)
                embed.set_image(url=data['file'])
        
        await self.ctx.reply(embed=embed, view=self , mention_author=False)
    
class fox_view(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.url = "http://randomfox.ca/floof/"
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
            async with aiohttp.ClientSession() as cs:
                async with cs.get(self.url) as r:
                    data = await r.json()
                    self.json_url = data['image']

                    embed = discord.Embed(title="Fox" , color=0xffffff)
                    embed.set_image(url=data['image'])

        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(emoji="💖", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        if self.ctx.author.id == interaction.user.id:
            self.add_button()
            await interaction.response.edit_message(view=self)
            self.stop()

    async def api_start(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.url) as r:
                data = await r.json()
                self.json_url = data['image']

                embed = discord.Embed(title="Fox" , color=0xffffff)
                embed.set_image(url=data['image'])
        
        await self.ctx.reply(embed=embed, view=self , mention_author=False)