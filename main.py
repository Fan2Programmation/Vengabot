import discord
from discord.ext import commands
import random
import config
from insulte import *


vengabot = commands.Bot(command_prefix='?')


@vengabot.event
async def on_ready():
    print("c'est bon panique pas")


@vengabot.event
async def on_message(ctx):
    insultes = [
        "keskia couzin pourquoi tu m'@",
        "oh le zinc ca va en maude robot ou quoi"
    ]
    if 'vengabot' in ctx.content.lower():
        await ctx.channel.send(random.choice(insultes))
    await vengabot.process_commands(ctx)


@vengabot.command(name='pet')
async def fart(ctx):
    if ctx.author.voice is None:
        await ctx.channel.send("T'es pas dans un vocal mon con")
    else:
        await ctx.author.voice.channel.connect()


# @vengabot.event
# async def on_typing(channel, user, when):
#     nom = str(user)[:-5]
#     await channel.send("arrete d'écrire mon reuf " + nom)


@vengabot.command(name='del')
async def delete(ctx, num: int):
    messages = await ctx.channel.history(limit=num + 1).flatten()
    for each in messages:
        await each.delete()


@vengabot.command(name='insulte')
async def insulte(ctx):
    await ctx.channel.send(getInsulte())
vengabot.run(config.key())
# plus qu'a avancer sur le pet, del fonctionne à merveille
