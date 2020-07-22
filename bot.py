import discord 
from discord.ext import commands
import json
import random
import os

with open ('setting.json', 'r', encoding='utf8') as jfile:
 jdata = json.load(jfile)
 
#註解符號的啦

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
  print(">>機器人上線囉<<")

@bot.event
async def on_member_join(member):
  channel =bot.get_channel(int(jdata['exit']))
  await channel.send(F'{member}加入伺服器!')

@bot.event
async def on_member_remove(member):
  channel =bot.get_channel(int(jdata['exit']))
  await channel.send(F'{member}離開伺服器!')

@bot.command()
async def load(ctx, extension):
  bot.load_extension(F'cmds.{extension}')
  await ctx.send(F'載入 {extension} 完成')

@bot.command()
async def unload(ctx, extension):
  bot.unload_extension(F'cmds.{extension}')
  await ctx.send(F'卸載 {extension} 完成')

@bot.command()
async def reload(ctx, extension):
  bot.reload_extension(F'cmds.{extension}')
  await ctx.send(F'重載 {extension} 完成')

for filename in os.listdir('./cmds'):
  if filename.endswith('.py'):
    bot.load_extension(F'cmds.{filename[:-3]}')

if __name__ == "__main__":
   bot.run(jdata['token'])

