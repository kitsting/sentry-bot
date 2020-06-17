# Work with Python 3.6
# {0.author.mention} = mention author
import discord
import random
import time
import os
from dotenv import load_dotenv
from discord.ext import commands
import keep_alive

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('DISCORD_PREFIX')
OWNER = os.getenv('OWNER')
COMPILE_TIME = time.ctime()
random.seed(COMPILE_TIME)

bot = commands.Bot(command_prefix=PREFIX)

bot.load_extension('bot_owner')
#bot.load_extension('bot_info')
bot.load_extension('bot_util')
bot.load_extension('bot_time')
bot.load_extension('bot_image')

@bot.event
async def on_ready():
    print("Logged in as " + str(bot.user.name) + " (ID: " + str(bot.user.id) + ")")
    await bot.change_presence(activity=discord.Game(name="Vanadius | Prefix: "+PREFIX))
    #bot.activity = discord.Game(name='g')

@bot.command(name='hello', help='Are you sure you want to do this???')
async def greetings(ctx):
    msg = '***loud screeching noise***'
    await ctx.send(msg)
    print('Saying hi...')

@bot.command(name='reload', help='OWNER ONLY: Reloads commands',hidden = 1)
@commands.is_owner()
async def reload(ctx, extension):
    await ctx.send('Reloading ' + str(extension) + '...')
    print('Reloading ' + str(extension) + '...')
    await bot.reload_extension(extension)

@bot.command(name='info', help='Lists bot info')
async def getinfo(ctx):
    embed = discord.Embed(title="Sentry Info", colour=discord.Colour(0x1))
    embed.set_footer(text="Last Run: " + COMPILE_TIME)
    embed.add_field(name=PREFIX, value="Prefix for all commands")
    embed.add_field(name="Other", value="This could be considered info i guess")
    await ctx.send(embed=embed)

@bot.command(name='invite', help='Get a link to put this... thing... in your server',hidden=1)
async def botinvite(ctx):
	await ctx.send('https://discordapp.com/api/oauth2/authorize?client_id=527617937268277258&permissions=0&scope=bot')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You fool, your permissions are wrong. Now perish.')
        print('User tried to access a command with invalid permissions')


keep_alive.keep_alive()

bot.run(TOKEN)