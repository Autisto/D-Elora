import discord
from discord.ext.commands import Bot
from discord.ext import commands
import requests

bot = Bot("*") 
client = discord.Client()

@client.event
async def on_ready():
    print('The Autist Is Here')

@bot.command()
async def hello(ctx, args):
    print('ctx.author.name')
    print('ctx.message')
    print('ctx.guild')

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("ip"):
        await message.channel.send("82.217.224.164:25701")

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("Hello"):

        if str(message.author) == "Sliganyth#0698":
            await message.channel.send("Hello you are a dipshit")
        else:
            await message.channel.send("Hello, Dipshit")
    if message.content.startswith("Fuck You"):
        await message.channel.send("Fuck You Too")

@client.event
async def on_message(message):
    if str(message.channel) == "memes" and message.content != "":
        await message.channel.purge(limit=1)



client.run('NjkyNzIwODg0NzI4NzI1NTE1.XnyomQ.L6t7jt7PG3IEEluN14dNViOdn0Y')