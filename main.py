import discord
import re
import os 
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')



url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
okay_links = []


#Configura a biblioteca
intents = discord.Intents.default()
intents.message_content = True


#Conecta com o discord
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("tamo online!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    #message.content

    if message.content.startswith('$add'):
        found_links = re.findall(url_pattern, message.content)

        for links in found_links:
            okay_links.append(links)
            await message.channel.send("Link Adicionado com Sucesso!")

    if re.search(url_pattern, message.content):
        found_links = re.findall(url_pattern, message.content)

        for link in found_links:
            for domain in okay_links:
                if not link.startswith(domain):
                    await message.delete()
                    await message.channel.send('Link Proibido, para adicionar um link use o comando $add')

client.run(token)

