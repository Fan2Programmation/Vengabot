import discord
from discord.ext import commands
import config

bot = commands.Bot(command_prefix='?')

@bot.command(name='re')
async def prog(ctx):
    await ctx.channel.send('on réessaie')

bot.run(config.key())