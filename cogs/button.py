# Standard 
import discord , asyncio
import datetime
from discord.ext import commands , tasks
from datetime import datetime, timezone , timedelta
from discord import Embed

# Third party
import aiohttp

# Local
from utils.waifu_pisc_api import *

class base_pisc_api(discord.ui.View):
    def __init__(self, ctx , url , title):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.title = title
        self.url = url
        self.json_url = ""  
        print(f"{self.title}\n{self.url}\n{self.json_url}")

    def add_button(self):
        self.add_item(discord.ui.Button(label='Image URL', url=self.json_url))

    async def on_timeout(self):
        self.clear_items()
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

            embed1 = API_waifu_im_Embed(self, json, title=self.title)
            for item in self.children:
                if item.label == "Image URL":
                    self.remove_item(item)
                    self.add_button()
                    
            await interaction.response.edit_message(embed=embed1, view=self)

    @discord.ui.button(emoji="❤️", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button, interaction):
        if self.ctx.author.id == interaction.user.id:
            self.clear_items()
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

        self.add_button()
        embed1 = API_waifu_im_Embed(self, json, title=self.title)
        await self.ctx.reply(embed=embed1, view=self, mention_author=False)

class Button_test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")

    @commands.command()
    async def test_view(self, ctx):
        url = "https://api.waifu.pics/sfw/waifu"
        title = "Waifu"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()
        #view.stop()
    
    @commands.command()
    async def test_view2(self, ctx):
        url = "https://api.waifu.pics/sfw/neko"
        title = "Neko"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()
        #view.stop()
        
def setup(bot):
    bot.add_cog(Button_test(bot))