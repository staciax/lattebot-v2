import aioimgur, discord, random, sr_api, asyncdagpi, aiogtts
import os, io, typing, datetime

def profile_converter(name):
  
  names_to_emojis = {
    "staff" : "<:staff:864052110450884609>",
    "partner" : "<:discordpartner:864052529729896458>",
    "hypesquad" : "<:hypesquad:864052223377670155>",
    "bug_hunter" : "<:bughunter:864052207237726218>",
    "hypesquad_bravery" : "<:bravery:864052291544154132>",
    "hypesquad_brilliance" : "<:brillance:864052307087589377>",
    "hypesquad_balance" : "<:balance:864052284707176449>",
    "early_supporter" : "<:supporter:864052229246156811> ",
    "system" : "<:system_badge:864053001237037067>",
    "bug_hunter_level_2" : "<:bug_hunter_level_2:864052216946753556>",
    "verified_bot" : "<:verified_BOT1:864060610911928320><:verified_BO2:864060626573590538>",
    "verified_bot_developer" : "<:verified_bot_developer:864053432468897812>",
    "early_verified_bot_developer" : "<:early_verified_bot_developer:864053963169726484>",
    "discord_certified_moderator" : "<:certified_moderator:864054307367682059>",
    "bot" : "<:bot1:864064664256905227><:bot2:864064720504094732>",
    "guildboost" : "<a:boost:864076334497923072>",
    "nitro" : "<:nitro:864052236103581716>",   
  }
  
  return names_to_emojis.get(name)
