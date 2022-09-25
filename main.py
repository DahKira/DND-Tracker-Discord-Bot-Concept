import discord
from discord.ext import commands
import os
import random

TOKEN = ''


intents = discord.Intents.all()
description = ''
bot = commands.Bot(command_prefix = 'dw!', description = description, intents = intents)


@bot.command()

async def info(ctx):


#will add to this later

	info = discord.Embed(title = 'Info')

	await ctx.send(embed=info)


@bot.command()

async def roll(ctx):

#dice rolling

	results = []


	divider = ctx.message.content.find(':')


	times = ctx.message.content[8:(divider)]


	TIMES = int(times)

	divider += 1


	sides = ctx.message.content[(divider):]


	SIDES = int(sides)

	while TIMES > 0:


		result = random.randint(0,(SIDES))

		results.append(result)


		TIMES -= 1


	RESULTS = str(results)


	total = sum(results)

	final_result = discord.Embed(title = 'Result', description = RESULTS[1:-1])


	final_result.add_field(name = 'Total', value = total)


	await ctx.send(embed=final_result)


@bot.command()

async def spells(ctx):


#bunch of data for spell embeds, squid focus here if possible my hands can't take this part of the bot

	interger = ctx.message.content[10:]


	acid_splash_EMBED = discord.Embed(title = 'Info - acid splash')


	acid_splash_EMBED.add_field(name = 'Spell Level', value = 'Cantrip')

	acid_splash_EMBED.add_field(name = 'School', value = 'Conjuration')

	acid_splash_EMBED.add_field(name = 'Classes', value = 'Wizard, Sorcerer')

	acid_splash_EMBED.add_field(name = 'Casting Time', value = '1 action')

	acid_splash_EMBED.add_field(name = 'Duration', value = 'Instantaneous')

	acid_splash_EMBED.add_field(name = 'Range', value = '60 feet')

	acid_splash_EMBED.add_field(name = 'Damage', value = '1d6')

	acid_splash_EMBED.add_field(name = 'Target', value = 'Either one or two, as long as they are within 5 feet of each over.')

	acid_splash_EMBED.add_field(name = 'Description', value = 'You throw a bubble-like formation of acid at your target(s).')

	acid_splash_EMBED.add_field(name = 'Extra', value = 'Damage increase by 1d6 at level 5 (2d6), level 11 (3d6) and level 17 (4d6).')


	chill_touch_EMBED = discord.Embed(title = 'Info - chill touch')


	chill_touch_EMBED.add_field(name = 'Spell Level', value = 'Cantrip')

	chill_touch_EMBED.add_field(name = 'School', value = 'Necromancy')

	chill_touch_EMBED.add_field(name = 'Classes', value = 'Wizard, Sorcerer, Warlock')

	chill_touch_EMBED.add_field(name = 'Casting Time', value = '1 action')

	chill_touch_EMBED.add_field(name = 'Duration', value = '1 round')

	chill_touch_EMBED.add_field(name = 'Range', value = '120 feet')

	chill_touch_EMBED.add_field(name = 'Damage', value = '1d8 necrotic')

	chill_touch_EMBED.add_field(name = 'Target', value = 'The space of a creature')

	chill_touch_EMBED.add_field(name = 'Description', value = 'You create a skeletal hand that holds onto your target for the rest of the turn if it does not miss.')

	chill_touch_EMBED.add_field(name = 'Extra', value = 'If it hits the target can not regain HP until your next turn. If it hits an undead it has disadvantage on attack rolls on you until your next turn. Damage increases by 1d8 when you reach level 5 (2d8), level 11 (3d8), level 17 (4d8).')

#sends out the info after detecting the user's requested spell

	if interger == 'acid splash':


                await ctx.send(embed=acid_splash_EMBED)


	if interger == 'chill touch':


		await ctx.send(embed=chill_touch_EMBED)



bot.run(TOKEN)
