import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}#{bot.user.discriminator}")

cogs_list = ["cogs.moderation", "cogs.greetings", "cogs.entertainment", "cogs.gpt"]

@bot.event
async def setup_hook():
    for cogs in cogs_list:
        await bot.load_extension(cogs)

bot.run(os.getenv("TOKEN"))