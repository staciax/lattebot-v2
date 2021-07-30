# Standard 
import discord , datetime , time , random 
from discord.ext import commands
from datetime import datetime, timezone

# Third party
import giphy_client 
from giphy_client.rest import ApiException

# Local
from config import *
from utils import text_to_owo , notify_user


class Images(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gif(self, ctx,*,q="random"):

        api_instance = giphy_client.DefaultApi()
        api_key = GIPHYAPI

        try: 
        
            api_response = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
            lst = list(api_response.data)
            giff = random.choice(lst)

            emb = discord.Embed(title=q,color=0xffffff)
            emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

            await ctx.channel.send(embed=emb)
        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

def setup(client):
    client.add_cog(Images(client))