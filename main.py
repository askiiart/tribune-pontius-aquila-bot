import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

intents = discord.Intents.none()
intents.messages = True
intents.message_content = True
client = commands.Bot(command_prefix="/", intents=intents)
token = os.getenv('TOKEN')

@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

@commands.command(name='aquila')
async def ping(ctx):
    await ctx.send("Who gave permission for this? I sure as hell didn't.")

client.run(token)
