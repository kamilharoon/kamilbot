import discord
from discord.ext import commands

prefix = "!"
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")

@bot.event
async def on_ready():
    bot.loop.create_task(status_task())
    print("Started successfully")

async def status_task():
    await bot.change_presence(activity=discord.Game("online"),
                              status=discord.Status.online)


@bot.command()
async def hello(ctx, member: discord.Member):
    await ctx.send(f"{ctx.author.name} sends you an hello {member}")
@bot.command()
async def help(ctx):
    await ctx.send(f"Commands: hello [user]")
    @bot.command()
    async def hi(ctx):
        await ctx.send(f"Commands:Welcome @shaheenkk#6300")

bot.run(" BOt token ")



