# Standard 
import discord
import datetime
from discord.ext import commands, menus
from discord import Embed

# Third party
import aiohttp

#-------------------- WAIFU IM --------------------#

class base_waifu_im_api(discord.ui.View):
    def __init__(self, ctx, url):
        super().__init__(timeout=600)
        self.ctx = ctx
        self.url = url
        self.image_url = ""
        self.message = ""
        self.gif = False
        self.source_url = ''

    def add_button(self):
        self.add_item(discord.ui.Button(label='Image URL', url=self.image_url))
    
    def api_site(self):
        self.add_item(discord.ui.Button(label='API site', url="https://waifu.im/"))

    async def on_timeout(self):
        self.clear_items()
        if self.message:
            await self.message.edit(view=self)
    
    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        role = discord.utils.get(self.ctx.guild.roles, id=842304286737956876)
        if interaction.user == self.ctx.author or role in interaction.user.roles:
            return True
        await interaction.response.send_message('This interaction cannot be controlled by you, sorry!', ephemeral=True)
        return False

    @staticmethod
    def Waifu_im_Embed(api_title, api_color, image_url):
        embed = Embed(title=api_title, url=image_url, color=int(api_color)) #timestamp=discord.utils.utcnow(),
        embed.set_image(url=image_url)
        embed.set_footer(text="Powered by waifu.im")
        
        return embed

    @staticmethod
    async def base_embed(self):
        async with aiohttp.ClientSession() as session:
            request = await session.get(f'{self.url}/?gif={self.gif}')
            api = await request.json()
            if request.status == 200:
                api_title = api.get('tags')[0].get('name')
            
                #color_converter
                dominant_color1 = str(api.get('tags')[0].get('images')[0].get('dominant_color')).replace('#', '')
                dominant_color = int(dominant_color1, 16)

                api_color = dominant_color
                image_url = api.get('tags')[0].get('images')[0].get('url')
                source_url = api.get('tags')[0].get('images')[0].get('source')
                self.image_url = image_url
                self.source_url = source_url

            embed_api = self.Waifu_im_Embed(api_title, api_color, image_url)
            return embed_api

    @discord.ui.button(label='▶', style=discord.ButtonStyle.blurple, custom_id='b1')
    async def button_api(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.gif = False
        embed = await self.base_embed(self)
        for items in self.children:
            if isinstance(items, discord.ui.Button):
                if items.label == "Image URL":
                    self.remove_item(item=items)
                    self.add_button()
        if embed:
            await interaction.response.edit_message(embed=embed, view=self)
    
    @discord.ui.button(label="GIF", style=discord.ButtonStyle.blurple, custom_id='b3')
    async def gif_true_or_false(self, button, interaction):
        if self.url in ['https://api.waifu.im/sfw/maid', 'https://api.waifu.im/nsfw/maid', 'https://api.waifu.im/nsfw/selfies']:
            self.gif = False
        else:
            self.gif = True
        embed = await self.base_embed(self)
        if embed:
            await interaction.response.edit_message(embed=embed, view=self)
    
    @discord.ui.button(emoji="❤️", style=discord.ButtonStyle.blurple, custom_id='b2')
    async def disable_all_button(self, button:discord.ui.Button, interaction: discord.Interaction):
        self.clear_items()
        self.add_button()
        self.api_site()
        await interaction.response.edit_message(view=self)
        self.stop()

    async def api_start(self):
        self.gif = False
        embed = await self.base_embed(self)
        if embed:
            self.add_button()
            self.message = await self.ctx.reply(embed=embed, view=self, mention_author=False)