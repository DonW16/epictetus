import discord
import os
import asyncio
import random
import wikipediaapi

TOKEN = os.getenv('DISCORD_TOKEN')
QUOTE_FILE = 'quotes.txt'

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('/author'):
        author = message.content.split('/author ')[1]
        await search_author(author, message.channel)

async def search_author(author, channel):
    try:
        # Perform Wikipedia search for the author
        # You can use any library or API to perform the search
        # Here's an example using the Wikipedia API

        wiki_wiki = wikipediaapi.Wikipedia('en')
        page_py = wiki_wiki.page(author)
        
        if page_py.exists():
            await channel.send(page_py.fullurl)
        else:
            await channel.send(f"Author '{author}' not found on Wikipedia")
    except Exception as e:
        await channel.send(f"An error occurred: {str(e)}")

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