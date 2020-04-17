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

        print("getting US info")
        results2 = soup.find_all(class_="maincounter-number")
        deaths = results2[1].text.strip()#.text.strip()
        discharged = results2[2].text.strip()#.text.strip()
        currentcases = results2[0].text.strip()# - int(deaths.text.replace(',',''))+int(discharged.text.replace(',',''))
        print(currentcases)

        currentcases = str(int(currentcases.replace(',',''))-int(deaths.replace(',',''))-int(discharged.replace(',','')))
        currentcases = str(format(int(currentcases),',.0f'))

        percentinfected = format((int(currentcases.replace(',',''))/uspop)*100,'.3f')
        percentdead = format((int(deaths.replace(',',''))/uspop)*100,'.3f')

        #print(results2)
        await ctx.send("Active US Cases: " + currentcases+"\nUS Deaths: " + deaths+"\nRecovered: " + discharged)
        #await ctx.send("\nUS Deaths: " + deaths)
        #await ctx.send("Recovered: " + discharged)
        await ctx.send("About "+str(percentinfected)+"% of pop. are infected and "+str(percentdead)+"% have died.")

 #       print("Getting AZ info")
#       results3 = soup.find_all(class_="odd")
 #       print(results3)


def setup(bot):
    bot.add_cog(UpdateCommands(bot))