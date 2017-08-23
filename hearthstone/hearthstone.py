import discord
import requests
from discord.ext import commands

class Hearthstone:
    """Cog for searching Hearthstone cards"""
        
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def card(self, name):
        """Searches for a regular Hearthstone card"""

        r = requests.get('https://omgvamp-hearthstone-v1.p.mashape.com/cards/{}'.format(name), headers={'X-Mashape-Key':'sly1A6Ur3tmshrDtRbWe4q738Afxp1cnkhajsnWqVf9HMJ7ZOJ'}) 
        
        await self.bot.say(r.json()[0]['img'])
        await self.bot.say(r.json()[0]['flavor'])

    @commands.command()
    async def gcard(self, name):
        """Searches for a gold Hearthstone card"""

        r = requests.get('https://omgvamp-hearthstone-v1.p.mashape.com/cards/{}'.format(name), headers={'X-Mashape-Key':'sly1A6Ur3tmshrDtRbWe4q738Afxp1cnkhajsnWqVf9HMJ7ZOJ'}) 
        
        await self.bot.say(r.json()[0]['imgGold'])
        await self.bot.say(r.json()[0]['flavor'])

def setup(bot):
    bot.add_cog(Hearthstone(bot))
