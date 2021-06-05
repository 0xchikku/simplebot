import os
import discord
import random
import requests
import json
my_secret = os.environ['TOKEN']

client = discord.Client()

help = [
	'1.commands',
	'2.fun',
	'3.memes',
	'4.Q/A'
]

welcome = [
	'Hello',
	'Bonjour',
	'How you doing?',
	'Hey',
	'Whats up?'
]

def get_quote():
	response = requests.get('https://zenquotes.io/api/random')
	json_data = json.loads(response.text)
	quote = json_data[0]['q'] + ' -' + json_data[0]['a']
	return(quote)

@client.event
async def on_ready():
	print('Lets Go...')

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('hello'):
		await message.channel.send(random.choice(welcome))
	
	if message.content.startswith('help'):
		await message.channel.send(help)

	if message.content.startswith('quote'):
		quote = get_quote()
		await message.channel.send(quote)

client.run(my_secret)