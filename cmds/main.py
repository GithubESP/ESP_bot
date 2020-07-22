import discord 
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):

 
    @commands.command()
    async def ping(self,ctx):
     await ctx.send(F'Ping值為{round(self.bot.latency*1000)}(毫秒)')

def setup(bot):
    bot.add_cog(Main(bot))
