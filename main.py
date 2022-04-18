import discord
from discord.ext import commands
import pynacl
import config

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print("c'est bon panique pas")

@bot.command(name='re')
async def prog(ctx):
    await ctx.channel.send('on réessaie')

@bot.command(name='pet')
async def fart(ctx):
    if ctx.author.voice is None:
        await ctx.channel.send("T'es pas dans un vocal mon con")
    else:
        await ctx.author.voice.channel.connect()

bot.run(config.key())