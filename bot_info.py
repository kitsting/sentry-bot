from discord.ext import commands
from dotenv import load_dotenv



class InfoCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    # @commands.command(name='info', help='Lists bot info')
    # async def getinfo(self, ctx):
    #     embed = discord.Embed(title="Sentry Info", colour=discord.Colour(0x1))
    #     embed.set_footer(text="Last Run: " + COMPILE_TIME)
    #     embed.add_field(name=PREFIX, value="Prefix for all commands")
    #     embed.add_field(name="Other", value="This could be considered info i guess")
    #     await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(InfoCommands(bot))
