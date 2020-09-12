import os
import discord
import time
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv("tokens.env")
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        for g in self.guilds:
            print(f'Conencted to {g}')


bot = commands.Bot(command_prefix='!')


@bot.command(name='fuck', help='Type !fuck to fuck something.')
async def fuck(ctx, *, thing):
    await ctx.send(f'Fuck {thing}')

@bot.command(name='chaser', help='Who is the chaser?')
async def chaser(ctx):
    voice_channel = ctx.author.voice.channel
    channel = None
    if voice_channel is not None:
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(source='chaser_walk_on.mp3'))
        while vc.is_playing():
            time.sleep(1)
        await vc.disconnect()
    else:
        await ctx.send(f'{str(ctx.author.name)} not in a channel.')

bot.run(TOKEN)

#client = CustomClient()
#client.run(TOKEN)
