from discord.ext import commands

class OwnerCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(name='owner',help='OWNER ONLY, used for testing',hidden=1)
    @commands.is_owner()
    async def ownertest(self, ctx):
        #if ctx.author != is_owner
            #return
        await ctx.send(ctx.author)


    @commands.command(name='begone',help="OWNER ONLY, I don't belong in this world",hidden=1)
    @commands.is_owner()
    async def begone(self, ctx):
        await ctx.send("I don't belong in this world")
        print('Logging out...')
        await self.bot.close()


def setup(bot):
    bot.add_cog(OwnerCommands(bot))
