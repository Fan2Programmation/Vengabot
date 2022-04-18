import discord
from discord.ext import commands
import random
import config

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print("c'est bon panique pas")

@bot.event
async def on_message(message):
  insultes = [
    "keskia couzin pourquoi tu m'@",
    "oh le zinc ca va en maude robot ou quoi"
  ]
  if 'vengabot' in message.content.lower():
    await message.channel.send(random.choice(insultes))

@bot.command(name='pet')
async def fart(ctx):
    if ctx.author.voice is None:
        await ctx.channel.send("T'es pas dans un vocal mon con")
    else:
        await ctx.author.voice.channel.connect()

bot.run(config.key())