import os
import discord
from dotenv import load_dotenv
import pandas_datareader as web

client = discord.Client()

load_dotenv()
TOKEN = os.getenv("TOKEN")

#GET THE REAL-TIME PRICE OF STOCKS IN THE MARKET
def get_stock_price(ticker):
    data = web.DataReader(ticker, "yahoo")
    return data['Close'].iloc[-1]

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send("Hello World! I am ElCruzo!")
        
    if message.content == '$personal':
        await message.author.send("Hellooooooo!")
        
    if message.content.startswith('$stockprice'):
        if len(message.content.split(" ")) == 2:
            ticker = message.content.split(" ")[1]
            price = get_stock_price(ticker)
            get_stock_price(ticker)
            await message.channel.send(f"Stock price of {ticker} is {price}!") 

@client.event
async def on_connect():
    print("Bot connected to the server!")
    channel = client.get_channel(12345678)
    # await channel.send("Just connected to the bot-commands!")

async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Welcome To The Server {member}!")

client.run(TOKEN)