import discord
from discord.ext import commands
import random
import config
from insulte import *
import youtube_dl
import os
from discord import FFmpegPCMAudio

import yt_dlp

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


@vengabot.command(name='musicYT')
async def musicYT(ctx, url: str):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
        source = FFmpegPCMAudio("song.mp3")
        player = voice.play(source)

    else:
        await ctx.channel.send("T'es pas dans un vocal mon con")


# @vengabot.command(name='stop')
# async def stop(ctx):
#     test = ctx.bot.is_connected
#     print(test)


@vengabot.command(name='insulte')
async def insulte(ctx):
    await ctx.channel.send(getInsulte())
vengabot.run(config.key())
# plus qu'a avancer sur le pet, del fonctionne à merveille
