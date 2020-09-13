import os
import discord
import time
import random
from discord.ext import commands
from dotenv import load_dotenv
from make_gif import make_gif

print('Loading tokens...')

load_dotenv("tokens.env")
TOKEN = os.getenv('DISCORD_TOKEN')
kill_pw = os.getenv('KILL_PW')
#GUILD = os.getenv('DISCORD_GUILD')

print('Building bot...')

names = ["Simon", "Jamie", "James", "Alex", "Sam", "Elliott", "Jacob", "Will", "Ned", "Jake", "Chappers"]
thinking = ["Hmmm let me think.", "This is an easy one.", "Now this is HLTV confirmed.", "Tricky one...", "Errrm.",
            "OK this one is close.", "Stupid question..."]


class CustomClient(discord.Client):
    async def on_ready(self):
        print("{} has connected to Discord!".format(self.user))
        for g in self.guilds:
            print("Connected to {}".format(g))


bot = commands.Bot(command_prefix='!')


@bot.command(name='kill', help='Protected kill command. Shuts off bot.')
async def kill(ctx, *, pw):
    await ctx.message.delete()
    if str(pw) == kill_pw:
        await ctx.send("Putting bot to sleep...")
        await bot.logout()
    else:
        await ctx.send("No permission to kill bot.")


@bot.command(name='repeat', help='Type !repeat to fuck something.')
async def repeat(ctx, *, thing):
    await ctx.send("Fuck {}".format(thing))


@bot.command(name='who', help='Type !who is blank thing to decide who is a thing.')
async def who(ctx, *, thing):
    await ctx.send(random.choice(thinking))
    thing = thing.replace("?", "")
    #if thing[0:3] == "is ":
    #   thing = thing[3:]
    time.sleep(1)
    await ctx.send("{} {}.".format(random.choice(names), thing), tts=True)
    #await ctx.message.delete()


@bot.command(name='chaser', help='Who is the chaser?')
async def chaser(ctx):
    voice_channel = ctx.author.voice.channel if ctx.author.voice is not None else None
    channel = None
    if voice_channel is not None:
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(source='chaser_walk_on.mp3'))
        while vc.is_playing():
            time.sleep(1)
        await vc.disconnect()
    else:
        await ctx.send("{} is not in a channel.".format(str(ctx.author.name)))
    await ctx.message.delete()


@bot.command(name='goal', help='BBC WM Goal Horn')
async def goal(ctx):
    voice_channel = ctx.author.voice.channel if ctx.author.voice is not None else None
    channel = None
    if voice_channel is not None:
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(source='WM_Goal.mp3'))
        while vc.is_playing():
            time.sleep(1)
        await vc.disconnect()
    else:
        await ctx.send("{} is not in a channel.".format(str(ctx.author.name)))
    await ctx.message.delete()


@bot.command(name='retard', help='m0e asks a question')
async def retard(ctx):
    voice_channel = ctx.author.voice.channel if ctx.author.voice is not None else None
    channel = None
    if voice_channel is not None:
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(source='audio/retard_m0e.mp3'))
        while vc.is_playing():
            time.sleep(1)
        await vc.disconnect()
    else:
        await ctx.send("{} is not in a channel.".format(str(ctx.author.name)))
    await ctx.message.delete()


@bot.command(name='fuck', help='Steel finds out @tomi is still tweeting')
async def fuck(ctx):
    voice_channel = ctx.author.voice.channel if ctx.author.voice is not None else None
    channel = None
    if voice_channel is not None:
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(source='audio/fuck.mp3'))
        while vc.is_playing():
            time.sleep(1)
        await vc.disconnect()
    else:
        await ctx.send("{} is not in a channel.".format(str(ctx.author.name)))
    await ctx.message.delete()


@bot.command(name='shitting', help='Steel has piles?')
async def shitting(ctx):
    voice_channel = ctx.author.voice.channel if ctx.author.voice is not None else None
    channel = None
    if voice_channel is not None:
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(source='audio/shitting_me.mp3'))
        while vc.is_playing():
            time.sleep(1)
        await vc.disconnect()
    else:
        await ctx.send("{} is not in a channel.".format(str(ctx.author.name)))
    await ctx.message.delete()


@bot.command(name='defuse', help='For trolling only.')
async def defuse(ctx):
    voice_channel = ctx.author.voice.channel if ctx.author.voice is not None else None
    channel = None
    if voice_channel is not None:
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(source='audio/defuse.mp3'))
        while vc.is_playing():
            time.sleep(1)
        await vc.disconnect()
    else:
        await ctx.send("{} is not in a channel.".format(str(ctx.author.name)))
    await ctx.message.delete()


@bot.command(name='idgi', help='I don\'t get it')
async def idgi(ctx):
    channel = ctx.message.channel
    await channel.send(file=discord.File('idgi.jpg'))
    voice_channel = ctx.author.voice.channel if ctx.author.voice is not None else None
    channel = None
    if voice_channel is not None:
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(source='audio/idgi.mp3'))
        while vc.is_playing():
            time.sleep(1)
        await vc.disconnect()
    await ctx.message.delete()

@bot.command(name='qi', help='ALARM - !qi text')
async def qi(ctx, *, text):
    channel = ctx.message.channel
    await ctx.message.delete()
    print(text)
    await channel.send(file=discord.File(make_gif(text)))
    voice_channel = ctx.author.voice.channel if ctx.author.voice is not None else None
    channel = None
    if voice_channel is not None:
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(source='audio/qi.mp3'))
        while vc.is_playing():
            time.sleep(1)
        await vc.disconnect()


print('Bot starting!')
bot.run(TOKEN)

#client = CustomClient()
#client.run(TOKEN)
