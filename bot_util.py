from discord.ext import commands
import random
import time
import math

def GetRand():
    random.seed(time.ctime())
    ii = random.randint(0, 1)
    if ii != 0:
        return 0
    if ii == 0:
        return str(random.randint(1, 100))

class UtilCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='thotdect', help='Thot detector for easier crusades')
    async def thotdect(self, ctx, user: str = 0):
        if user != 0: user = user
        if user == 0: user = ctx.author
        #await ctx.send('f')
        await ctx.send(str(user) + " is " + str(GetRand()) + "% thot") #str(GetRand())


    @commands.command(name='vanfact', help='Returns a random fact about Vanadius')
    async def vanfact(self, ctx):
        vanadiusfacts = [
            'Collectibles with red sparkles will set your spawn point.',
            'Most sentries have depression. This is because nobody has played Vanadius.',
            'Sentries very slightly speed up after a short time of chasing you. Eventually, they can get so fast they start yeeting.',
            'There are 15 collectibles in Vanadius. In version 1.0, a rare bug can occur which allows you to get more than 15.',
            'Vanadius\'s save files aren\'t encrypted. This means it\'s easy to modify save data in an unintended way.',
            'There was originally going to be a way to get back to the Cave area of the game.',
            'If you return to the Deep Lab after completing it, you get to access the hideout of the Big Sentry, among a few other small changes.',
            'There used to be green flasks, which would home in on the player. As time went on, they would spin faster and faster until eventually exploding. They can still be found in the testing room',
            'The testing room can be accessed by getting all 15 collectibles and going through a very challenging area in the Power Plant.',
            'Purple flasks were originally missiles.',
            'The gears in the Clock Tower originally looked like green Sentries.',
            'An early concept for a sentry was the Missile Sentry. It would shoot missiles at the player if they got too close. The idea was scrapped and the sprite was used for normal sentries.',
            'There were plans for an icy area near the end of the game. This idea was scrapped after implementation of ice failed horribly.',
            'There were plans for a speed boosting tile. The player would gain more speed the longer they walked on it. This proved to be buggy and has since been removed.',
            'Vanadius devlogs are available on Twitter by @KSticcGames if you scroll down far enough.',
            'There were originally safe areas, that, when stepped in, would cause sentries to retreat. These were replaced by safety pressure plates, which were removed late in development.',
            'Most of the tilesets in the game went through many iterations, so the final ones are about the 3rd or 4th iteration.',
            'Vanadius is available to download for Windows at ksting.itch.io/vanadius.',
            'One of the lore signs states that a previous subject has escaped. The only reason this exists is to set up for a possible prequel.',
            'There are many inherent issues reported by the 3 people who have played the game, such as "The robot walks to slow" and "The pixel art is too chunky".',
            'Vanadius took about a year and a half to develop using GameMaker Studio 2.',
            'A bug in version 1.1 causes the game to not start at all due to an incorrect file dependency. This could have been easily avoided with one line of code.',
            'A corrupted version of the game exists where ui elements are buggy and text is wildly incorrect',
            'In early builds of the game, a larger, thinner font was used. This was scrapped in favor of a custom font.',
            'The earliest known prototype for Vanadius dates back to April of 2018',
            'Multiple sprites went unused during development. One of these includes the player looking down at the floor, as if depressed.',
            'An early sprite for falling had the player in a t-pose like position as they fell. This animation was removed as it didn\'t fit the perspective.',
            'An early sprite, called \'battlebot.png\', shows a subject seemingly fused with a sentry. These enemies would have appeared in the Power Plant and they would have shot missiles.',
            'Various unused themes for areas were planned. These include an underground shipwreck, an icy area, and an area whose main mechanics would have been fire and water.',
            'The Clock Tower was originally going to be a bonus level.',
            'Various ideas go unused from the planning stages of development, such as moving platforms and glass walls.',
            'The only reason Vanadius exists is because the idea of having to sneak around like the Green Arrow sounded cool. Ultimately, the game turned out to be nothing like that.',
            'In the very, very early brainstorming stages, Vanadius was originally planned to be a metroidvania. This idea may still be acted upon.',
            'Most of the ideas from the original planning drawing made it into the final game one way or another.',
        ]
        await ctx.send("Fun Fact: " + random.choice(vanadiusfacts))


    @commands.command(name = 'copypasta', help = 'Returns Copypasta. Arguments: idk',hidden=1)
    async def copypasta(self, ctx, type='none'):
        if type == 'idk':
            await ctx.send('''Idk is an abbreviation of the phrase I don’t know. Idk is part of the newly developed dialect called text speak or SMS language. This dialect is mostly used in informal communication, and especially when communicating via text messages or instant messages. The phrase idk has been part of text speak since at least 2002.
            
You can use idk the same way you use the phrase I don’t know. In informal writing, and especially in text messages, the rules of capitalization are lax at best, so you can choose how you want to treat idk. The one rule that has come about in text speak is that writing a word in all caps means you’re either shouting it or are otherwise trying to emphasize it or amplify its effect. If you’re using idk in a more formal context, you should always make sure you capitalize it—or not—consistently.''')

        if type != 'idk':
            await ctx.send('You most specify and argument you fool')


    @commands.command(name = 'bruh', help = 'Bruh Moment')
    async def bruh(self,ctx):
        bruh_moments = [
            'Bruh Moment',
            'This is a certified Bruh Moment',
            'Bruh',
        ]
        await ctx.send(random.choice(bruh_moments))


    @commands.command(name = 'sentryspeed', help = 'Calculate the speed of a sentry. Arguments: Time in seconds')
    async def sentryspeed(self,ctx,secs=0):
        print(secs)
        if isinstance(secs,int):
            base_speed = 5
            added = secs/5
            speedtime = base_speed+added
            await ctx.send('A Sentry would be moving '+str(speedtime)+'MPH after '+str(secs)+' seconds')
        else:
            await ctx.send('Give a time in whole seconds.')


def setup(bot):
    bot.add_cog(UtilCommands(bot))