import discord
from discord.ext import commands
import random

bot = commands.Bot()


@bot.slash_command(name="help", description="info on the bot")
async def help(ctx):

    help_embed = discord.Embed(title='Help')

    help_embed.add_field(name='roll', value='Roll a dice.')
    help_embed.add_field(name='github', value='https://github.com/DahKira/Iori')

    await ctx.respond(embed=help_embed)

@bot.slash_command(name="roll", description="Roll dice")
async def roll(ctx, number: int, sides: int, mod: int):

    print('> Recieving roll command request')

    results = []

    loop = number

    while loop > 0:


         rolled = random.randint(1,(sides))

         results.append(rolled)

         loop -= 1


    if not mod == 0:

         results.append(mod)


    resultsS = str(results)

    resultsS = resultsS[1:-1]

    if mod == 0:

         reply = '``'+resultsS+'`` | ``'+str(number)+'d'+str(sides)+'`` | ``total '+str(sum(results))+'``'

    if not mod == 0:

         reply = '``'+resultsS+'`` | ``'+str(number)+'d'+str(sides)+'`` | ``mod '+str(mod)+'`` | ``total '+str(sum(results))+'``'

    await ctx.respond(reply)

bot.run('') #place your bots token here
