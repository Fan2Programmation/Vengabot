import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print("bot prêt")

@bot.command(name='1')
async def premier(ctx):
    print("premier passe")

@bot.command(name='2')
async def deuxieme(ctx):
    print("deuxieme passe")

@bot.command(name='3')
async def troisieme(ctx):
    print("troisieme passe")

@bot.command(name='4')
async def quatrieme(ctx):
    print("quatrieme passe")
