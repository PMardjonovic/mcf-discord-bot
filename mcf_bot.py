import os
import discord

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
guild = discord.Guild

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == "mcf-bot":
        response = "Hello! I am the MCF bot."
        await message.channel.send(response)
    
client.run(TOKEN)
