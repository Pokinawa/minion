import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

	await client.change_presence(game=discord.Game(name = 'Say !help'))

@client.event
async def on_message(message):

	if message.content.startswith('!help'):
		await client.send_message(message.author, 'Commands coming soon - JJ')

client.run('MjMzODkwNDMwNTc0NTI2NDY0.CvP2Cw.E5AfVB-P8GXDhECSWkYwwHqvrNI')
