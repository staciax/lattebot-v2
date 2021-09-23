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

