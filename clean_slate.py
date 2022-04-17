import discord
from discord.ext import commands
import config

bot = commands.Bot(command_prefix='?')

@bot.command(name='test')
async def essai(ctx):
    await ctx.channel.send('bravo pour cet essai fructueux')

bot.run(config.key())