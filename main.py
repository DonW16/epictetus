import discord
import os
import random

TOKEN = os.getenv('DISCORD_TOKEN')
QUOTE_FILE = 'quotes.txt'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    @client.event
    async def on_message(message):
        if message.content.startswith('/quote'):
            await read_quotes()

    async def read_quotes():
        try:
            with open(QUOTE_FILE, 'r') as file:
                quotes = file.readlines()
                random_quote = random.choice(quotes)
                await message.channel.send(random_quote.strip())
        except FileNotFoundError:
            print(f'Error: Quotes file "{QUOTE_FILE}" not found')

async def read_quotes():
    try:
        with open(QUOTE_FILE, 'r') as file:
            quotes = file.readlines()
            # Process the quotes as needed
            random_quote = random.choice(quotes)
            await message.channel.send(random_quote.strip())
    except FileNotFoundError:
        print(f'Error: Quotes file "{QUOTE_FILE}" not found')

client.run(TOKEN)