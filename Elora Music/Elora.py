import discord

token = "692720884728725515"

client = discord.client()

@client.event
async def on_ready():
    print(f"{client.user} Online")

    client.run(token)
