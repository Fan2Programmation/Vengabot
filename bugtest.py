import discord
from discord.ext import commands
import random
import config

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print("bot prêt")

# @bot.event
# async def on_message(message):
#     insultes = [
#         "keskia couzin pk tu m'@",
#         "oh le zinc en maude robot ou quoi"
#     ]
#     if 'vengabot' in message.content.lower():
#         await message.channel.send(random.choice(insultes))

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
async def troisieme(ctx):
    print("quatrieme passe")

bot.run(config.key())
