import os
import discord
import time
from discord.ext import commands
from dotenv import load_dotenv

print('Loading tokens...')

load_dotenv("tokens.env")
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

print('Building bot...')


class CustomClient(discord.Client):
    async def on_ready(self):
        print("{} has connected to Discord!".format(self.user))
        for g in self.guilds:
            print("Conencted to {}".format(g))


bot = commands.Bot(command_prefix='!')


@bot.command(name='fuck', help='Type !fuck to fuck something.')
async def fuck(ctx, *, thing):
    await ctx.send("Fuck {}".format(thing))

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

@bot.command(name='idgi', help='I don\'t get it')
async def idgi(ctx):
    channel = ctx.message.channel
    await channel.send(file=discord.File('idgi.jpg'))
    await ctx.message.delete()

print('Bot starting!')
bot.run(TOKEN)

#client = CustomClient()
#client.run(TOKEN)
