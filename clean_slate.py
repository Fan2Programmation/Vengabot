import discord
from discord.ext import commands
import config

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print('VENGABOT armé')

@bot.command(name='test')
async def essai(ctx):
    await ctx.channel.send('bravo pour cet essai fructueux')

@bot.event
async def on_message(message):
    text = message.content.lower()
    if 'vengabot' in text:
        await message.channel.send('ftg')

bot.run(config.key())