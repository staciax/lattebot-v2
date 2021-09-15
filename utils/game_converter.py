import discord , random
from discord import Embed
from discord.ext import commands

def apex_random_weapon(category):
    #embed
    embed = Embed(color=0xFFA500)

    #list_of_weapon
    Assault_rifles = ["HAVOC Rifle", "VK-47 Flatline", "Hemlok Burst AR" , "R-301 Carbine"]
    Submachine_guns = ["Alternator SMG","Prowler Burst PDW","R-99 SMG","Volt SMG"]
    Light_machine_guns = ["Devotion LMG" , "L-STAR EMG", "M600 Spitfire" , "Rampage"]
    Marksman_weapons = ["G7 Scout", "Triple Take", "30-30 Repeater", "Bocek Compound Bow"]
    Sniper_rifles = ["Charge Rifle", "Longbow DMR", "Kraber .50-Cal Sniper", "Sentinel"]
    Shotguns = ["EVA-8 Auto", "Mastiff Shotgun", "Mozambique Shotgun", "Peacekeeper"]
    Pistols = ["RE-45 Auto","P2020","Wingman"]
    all_weapon = ["HAVOC Rifle", "VK-47 Flatline", "Hemlok Burst AR" , "R-301 Carbine","Alternator SMG","Prowler Burst PDW","R-99 SMG","Volt SMG","Devotion LMG" , "L-STAR EMG", "M600 Spitfire" , "Rampage","G7 Scout", "Triple Take", "30-30 Repeater", "Bocek Compound Bow","Charge Rifle", "Longbow DMR", "Kraber .50-Cal Sniper", "Sentinel","EVA-8 Auto", "Mastiff Shotgun", "Mozambique Shotgun", "Peacekeeper","RE-45 Auto","P2020","Wingman"]

    #category
    if category == None:
        random_gun = random.choice(all_weapon)
    elif category == "help":
        embed.title = "APEX type guns"
        embed.set_footer(text=f"{PREFIX}apex <type>")
        random_gun = """
        `ar` • Assault rifles
        `sub` • Sub-machine guns
        `light` • Light machine guns
        `marksman` • Marksman weapons
        `sniper` • Sniper rifles
        `sg` • Shotguns
        `pt` • Pistols
        """
    elif category == "ar":
        random_gun = random.choice(Assault_rifles)
    elif category == "sub":
        random_gun = random.choice(Submachine_guns)
    elif category == "light":
        random_gun = random.choice(Light_machine_guns)
    elif category == "marksman":
        random_gun = random.choice(Marksman_weapons)
    elif category == "sniper":
        random_gun = random.choice(Sniper_rifles)
    elif category == "sg":
        random_gun = random.choice(Shotguns)
    elif category == "pt":
        random_gun = random.choice(Pistols)
    
    #picture_of_gun
    if random_gun == "HAVOC Rifle":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/e/ec/HAVOC_Rifle.png/revision/latest/scale-to-width-down/1000?cb=20190304144136")
    elif random_gun == "VK-47 Flatline":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/f/f1/VK-47_Flatline.png/revision/latest/scale-to-width-down/1000?cb=20190304143943")
    elif random_gun == "Hemlok Burst AR":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/7/74/Hemlok_Burst_AR.png/revision/latest/scale-to-width-down/1000?cb=20190304144048")
    elif random_gun == "R-301 Carbine":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/f/f1/R-301_Carbine.png/revision/latest/scale-to-width-down/1000?cb=20190304143302")
    elif random_gun == "Alternator SMG":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/e/e9/Alternator_SMG.png/revision/latest/scale-to-width-down/688?cb=20190304180240")
    elif random_gun == "Prowler Burst PDW":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/b/bf/Prowler_Burst_PDW.png/revision/latest/scale-to-width-down/996?cb=20190304180338")
    elif random_gun == "R-99 SMG":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/d/d5/R-99_SMG.png/revision/latest/scale-to-width-down/1000?cb=20190304180412")
    elif random_gun == "Volt SMG":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/f/f5/Volt.png/revision/latest/scale-to-width-down/1000?cb=20210717062422")
    elif random_gun == "Devotion LMG":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/8/8c/Devotion_LMG.png/revision/latest/scale-to-width-down/1000?cb=20190304180450")
    elif random_gun == "L-STAR EMG":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/0/01/L-STAR_EMG.png/revision/latest/scale-to-width-down/1000?cb=20190709153859")
    elif random_gun == "M600 Spitfire":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/f/f2/M600_Spitfire.png/revision/latest/scale-to-width-down/1000?cb=20190304180514")
    elif random_gun == "Rampage":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/e/e4/Rampage.png/revision/latest/scale-to-width-down/1000?cb=20210807042402")
    elif random_gun == "G7 Scout":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/e/eb/G7_Scout.png/revision/latest/scale-to-width-down/1000?cb=20190304181016")
    elif random_gun == "Triple Take":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/d/d9/Triple_Take.png/revision/latest/scale-to-width-down/1000?cb=20210823030642")
    elif random_gun == "30-30 Repeater":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/8/86/30-30_Repeater.png/revision/latest/scale-to-width-down/1000?cb=20210710054145")
    elif random_gun == "Bocek Compound Bow":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/0/02/Bocek_Compound_Bow.png/revision/latest/scale-to-width-down/777?cb=20210710045232")
    elif random_gun == "Charge Rifle":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/2/2b/Charge_Rifle.png/revision/latest/scale-to-width-down/1000?cb=20210130154504")
    elif random_gun == "Longbow DMR":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/4/46/Longbow_DMR.png/revision/latest/scale-to-width-down/1000?cb=20190304181103")
    elif random_gun == "Kraber .50-Cal Sniper":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/f/f5/Kraber_.50-Cal_Sniper.png/revision/latest/scale-to-width-down/1000?cb=20190304181037")
    elif random_gun == "Sentinel":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/9/91/Sentinel.png/revision/latest/scale-to-width-down/1000?cb=20210710095136")
    elif random_gun == "EVA-8 Auto":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/9/97/EVA-8_Auto.png/revision/latest/scale-to-width-down/1000?cb=20210817041450")
    elif random_gun == "Mastiff Shotgun":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/c/c9/Mastiff_Shotgun.png/revision/latest/scale-to-width-down/1000?cb=20210818084651")
    elif random_gun == "Mozambique Shotgun":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/a/ae/Mozambique_Shotgun.png/revision/latest/scale-to-width-down/1000?cb=20210813094328")
    elif random_gun == "Peacekeeper":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/6/64/Peacekeeper.png/revision/latest/scale-to-width-down/1000?cb=20210814095843")
    elif random_gun == "RE-45 Auto":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/2/25/RE-45_Auto.png/revision/latest/scale-to-width-down/1000?cb=20210816090119")
    elif random_gun == "P2020":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/c/c1/P2020.png/revision/latest/scale-to-width-down/1000?cb=20210815055000")
    elif random_gun == "Wingman":
        embed.set_image(url="https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/0/09/Wingman.png/revision/latest/scale-to-width-down/1000?cb=20210813090820")
    
    embed.description = f"**{random_gun}**"
    
    return embed

#valorant
def valorant_random_agent(category):
    #embed
    embed = discord.Embed(color=0xfa4454)

    #list_of_agent
    Duelist = ["Phoenix", "Jett", "Reyna", "Raze", "Yoru"]
    Controller = ["Brimston","Viper","Omen","Astra"]
    Initiator = ["Sova", "Breach", "KAY/O" "Skye"]
    Sentinel = ["Killjoy", "Cypher", "Sage"]
    all_agent = ["Phoenix", "Jett", "Reyna", "Raze", "Yoru", "Brimston","Viper","Omen","Astra", "Sova", "Breach", "KAY/O", "Killjoy", "Cypher", "Sage"]

    
    #category
    if category == None:
        random_agent = random.choice(all_agent)
    elif category == "help":
        embed.title = "Valorant Agent type"
        embed.set_footer(text=f"{PREFIX}vlr agent <type>")
        random_agent = """
        `duelist` • Type duelist
        `controller` • Type controller
        `initiator` • Type initiator
        `sentinel` • Type sentinel
        """
    elif category == "duelist":
        random_agent = random.choice(Duelist)
    elif category == "controller":
        random_agent = random.choice(Controller)
    elif category == "initiator":
        random_agent = random.choice(Initiator)
    elif category == "sentinel":
        random_agent = random.choice(Sentinel)
    
    #picture_of_agent
    if random_agent == "Phoenix":
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/valorant/images/1/14/Phoenix_icon.png/revision/latest/scale-to-width-down/256?cb=20201128234131")
    elif random_agent == "Jett":
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/valorant/images/3/35/Jett_icon.png/revision/latest/scale-to-width-down/256?cb=20201128234156")
    elif random_agent == "Reyna":
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/valorant/images/b/b0/Reyna_icon.png/revision/latest/scale-to-width-down/256?cb=20200607180311")
    elif random_agent == "Raze":
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/valorant/images/9/9c/Raze_icon.png/revision/latest/scale-to-width-down/256?cb=20201128234400")
    elif random_agent == "Yoru":
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/valorant/images/d/d4/Yoru_icon.png/revision/latest/scale-to-width-down/256?cb=20210112211830")
    elif random_agent == "Brimston":
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/valorant/images/4/4d/Brimstone_icon.png/revision/latest/scale-to-width-down/256?cb=20201128234311")
    elif random_agent == "Viper":
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/valorant/images/5/5f/Viper_icon.png/revision/latest/scale-to-width-down/256?cb=20201128234408")
    elif random_agent == "Omen":
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/valorant/images/b/b0/Omen_icon.png/revision/latest/scale-to-width-down/256?cb=20201128234318")
    elif random_agent == "Astra":
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/valorant/images/0/08/Astra_icon.png/revision/latest/scale-to-width-down/256?cb=20210302164234")
    elif random_agent == "Sova":
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/valorant/images/4/49/Sova_icon.png/revision/latest/scale-to-width-down/256?cb=20201128234221")
    elif random_agent == "Breach":
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/valorant/images/5/53/Breach_icon.png/revision/latest/scale-to-width-down/256?cb=20201128234328")
    elif random_agent == "KAY/O":
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/valorant/images/f/f0/KAYO_icon.png/revision/latest/scale-to-width-down/256?cb=20210622225019")
    elif random_agent == "Skye":
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/valorant/images/3/33/Skye_icon.png/revision/latest/scale-to-width-down/256?cb=20201128234628")
    elif random_agent == "Killjoy":
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/valorant/images/1/15/Killjoy_icon.png/revision/latest/scale-to-width-down/256?cb=20200805002141")
    elif random_agent == "Cypher":
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/valorant/images/8/88/Cypher_icon.png/revision/latest/scale-to-width-down/256?cb=20201128234211")
    elif random_agent == "Sage":
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/valorant/images/7/74/Sage_icon.png/revision/latest/scale-to-width-down/256?cb=20201128234057")
    
    embed.description = f"**{random_agent}**"

    return embed

def valorant_random_weapon(category):
    #embed
    embed = Embed(color=0xfa4454)

    #list_of_weapon
    all_gun = ["Classic","Shorty","Frenzy","Ghost","Sheriff","Stinger", "Spectre","Bucky", "Judge" , "Bulldog", "Guardian", "Phantom" , "Vandal" ,"Ares", "Odin" , "Knife"]
    Sidearms = ["Classic","Shorty","Frenzy","Ghost","Sheriff"]
    SMGs = ["Stinger", "Spectre"]
    Shotguns = ["Bucky", "Judge"]
    Rifles = ["Bulldog", "Guardian", "Phantom" , "Vandal"]
    Sniper_Rifles = ["Marshal", "Operator"]
    Machine_Guns = ["Ares", "Odin"]
#   Malee = "Knife"      

    #category
    if category == None:
        random_gun = random.choice(all_gun)
    elif category == "help":
        embed.title = "Valorant type guns"
        embed.set_footer(text=f"{PREFIX}vlr <type>")
        random_gun = """
        `side` • Sidearms
        `smg` • Sub-machine guns
        `sg` • Shotguns
        `ar` • Assault rifles
        `sniper` • Sniper Rifles
        `mg` • Machine Guns
        """
    elif category in ["sidearms", "sidearm","side","sa"]:
        random_gun = random.choice(Sidearms)
    elif category in ["smg", "smgs"]:
        random_gun = random.choice(SMGs)
    elif category in ["shotgun","shotguns","sg"]:
        random_gun = random.choice(Shotguns)
    elif category in ["rifles","rifle","ar"]:
        random_gun = random.choice(Rifles)
    elif category in ["sniper","Sniper Rifles"]:
        random_gun = random.choice(Sniper_Rifles)
    elif category in ["machine","machine gun","mg"]:
        random_gun = random.choice(Machine_Guns)
            
    #picture_of_gun
    if random_gun == "Classic":
        embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/5/57/Classic.png/revision/latest/scale-to-width-down/1000?cb=20200404154125")
    elif random_gun == "Shorty":
        embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/7/77/Shorty.png/revision/latest/scale-to-width-down/1000?cb=20200404154222")
    elif random_gun == "Frenzy":
        embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/f/f1/Frenzy.png/revision/latest/scale-to-width-down/1000?cb=20200404154617")
    elif random_gun == "Ghost":
        embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/a/ab/Ghost.png/revision/latest/scale-to-width-down/1000?cb=20200404154731")
    elif random_gun == "Sheriff":
        embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/3/3e/Sheriff.png/revision/latest/scale-to-width-down/1000?cb=20200404154438")
    elif random_gun == "Stinger":
        embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/b/b6/Stinger.png/revision/latest/scale-to-width-down/1000?cb=20200404170849")
    elif random_gun == "Spectre":
        embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/9/90/Spectre.png/revision/latest/scale-to-width-down/1000?cb=20200404170922")
    elif random_gun == "Bucky":
        embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/e/eb/Bucky.png/revision/latest/scale-to-width-down/1000?cb=20200404171832")
    elif random_gun == "Judge":
        embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/8/8a/Judge.png/revision/latest/scale-to-width-down/1000?cb=20200404171858")
    elif random_gun == "Bulldog":
        embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/0/07/Bulldog.png/revision/latest/scale-to-width-down/1000?cb=20200404171103")
    elif random_gun == "Guardian":
        embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/f/fd/Guardian.png/revision/latest/scale-to-width-down/1000?cb=20200404171224")
    elif random_gun == "Phantom":
        embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/e/ec/Phantom.png/revision/latest/scale-to-width-down/1000?cb=20200404171302")
    elif random_gun == "Vandal":
        embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/5/56/Vandal.png/revision/latest/scale-to-width-down/1000?cb=20200404171348")
    elif random_gun == "Marshal":
        embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/b/b9/Marshal.png/revision/latest/scale-to-width-down/1000?cb=20200404172126")
    elif random_gun == "Operator":
        embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/1/17/Operator.png/revision/latest/scale-to-width-down/1000?cb=20200404172152")
    elif random_gun == "Ares":
        embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/0/05/Ares.png/revision/latest/scale-to-width-down/1000?cb=20200404171957")
    elif random_gun == "Odin":
        embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/5/58/Odin.png/revision/latest/scale-to-width-down/1000?cb=20200404172022")
    elif random_gun == "Knife":
        embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/d/d8/TacticalKnife.png/revision/latest/scale-to-width-down/1000?cb=20200404172248")
    
    embed.description = f"**{random_gun}**"

    return embed