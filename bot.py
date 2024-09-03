import os
import discord
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

MOTIVATIONAL_PHRASES = [
    "Você não vai se dar por vencido não é, senpai?",
    "Continue, senpai! A vitória está próxima!",
    "Lembre-se, senpai, os desafios são apenas oportunidades disfarçadas!",
    "Não desista, senpai!!! Estou torcendo por você",
]

def get_random_motivation():
    return random.choice(MOTIVATIONAL_PHRASES)

@client.event
async def on_ready():
    print(f'{client.user} entrou no Discord!')
    print(f'{client.user}: Espero que você dê seu melhor, senpai!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!motiva'):
        response = get_random_motivation()
        await message.channel.send(response)
    
    elif message.content.startswith('!oi'):
        response = 'Olá, senpai!'
        await message.channel.send(response)

client.run(TOKEN)
