import discord
import os
from dotenv import load_dotenv

client = discord.Client()

load_dotenv()
TOKEN = os.getenv("TOKEN")

client.run(TOKEN)