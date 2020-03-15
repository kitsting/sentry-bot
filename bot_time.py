from discord.ext import commands
import requests
from bs4 import BeautifulSoup

uspop = 330436532

class UpdateCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="corona",help="Returns coronavirus updates")
    async def corona(self,ctx):
        page = requests.get("https://www.worldometers.info/coronavirus/country/us")
        soup = BeautifulSoup(page.content,'html.parser')
        print("getting cases")
        results1 = soup.find_all(class_="number-table-main")
        currentcases = results1[0]
        #print("Confirmed Active US Cases: "+currentcases.text)
        print("getting deaths")
        results2 = soup.find_all(class_="number-table")
        deaths = results2[3]
        discharged = results2[2]
        #print(int(currentcases.text))
        percentinfected = format((int(currentcases.text.replace(',',''))/uspop)*100,'.5f')
        #infectedfinal = format(percentinfected,'.5f')
        percentdead = format((int(deaths.text.replace(',',''))/uspop)*100,'.5f')


        #print(results2)
        await ctx.send("Confirmed Active US Cases: " + currentcases.text)
        await ctx.send("Confirmed US Deaths: "+deaths.text)
        await ctx.send("Discharged from Hospital/Recovered: " + discharged.text)
        await ctx.send("About "+str(percentinfected)+"% of pop. are infected and "+str(percentdead)+"% have died.")



def setup(bot):
    bot.add_cog(UpdateCommands(bot))