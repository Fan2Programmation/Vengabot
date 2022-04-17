from discord.ext import commands
import random
import config

vengabot = commands.Bot(command_prefix="v")


@vengabot.event
async def on_ready():
    print("VENGABOT prêt à faire des dingueries")


@vengabot.command(name='Del')
async def delete(context, num: int):
    messages = await context.channel.history(limit=num + 1).flatten()

    for each in messages:
        await each.delete()


@vengabot.event
async def on_message(message):
    phrases = ["oh le zinc ca va en maude robot ou quoi",
               "keskia couzin pk tu m @"]
    if "vengabot" in message.content.lower():
        await message.channel.send("".join(random.sample(phrases, 1)))


@vengabot.event
async def on_typing(channel, user, when):
    nom = str(user)[:-5]
    await channel.send("arrete d'écrire mon reuf " + nom)

vengabot.run(config.key())

#test pour tout repush