import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print("VENGABOT prêt à faire des dingueries")

@client.event
async def on_message(message):
    phrases = ["oh le zinc ca va en maude robot ou quoi", "keskia couzin pk tu m @"]
    if "vengabot" in message.content.lower():
        await message.channel.send("".join(random.sample(phrases, 1)))

client.run("OTY0OTA2MjAyNDQ0MjMwNjg3.Ylrc7Q.rgQ1KUbhz3N6-kmKF0AtWAWQQcg")