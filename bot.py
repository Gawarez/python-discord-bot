import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from connect import runCommandSSH

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='$', intents=intents)

# Pelo amor de deus não rodar isso como root
@bot.command()
async def run(ctx, commandSSH):
  response = runCommandSSH(commandSSH)
  try:
    await ctx.send(response)
  except discord.HTTPException:
    await ctx.send("Exceção: Sem dados para retornar!")

@bot.command()
async def reply(ctx, *args):
  arguments = ' '.join(args)
  await ctx.send(arguments)

# Quando o membro entrou na Guild
@bot.command()
async def joined(ctx, *, member: discord.Member):
  await ctx.send(f'{member} joined the guild on {member.joined_at}')

bot.run(TOKEN)