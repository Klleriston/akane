import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from config import DISCORD_TOKEN
from riot_api import get_user_id, get_history, get_game_details, get_ranked_data
from utils import get_random_motivation


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} entrou no Discord!')
    print(f'{bot.user}: Espero que você dê seu melhor, senpai!')

@bot.command(name='motiva')

async def motiva(ctx):
    response = get_random_motivation()
    await ctx.send(response)

@bot.command(name='oi')
async def oi(ctx):
    response = f'Olá, senpai! Eu sou a {bot.user}.'
    await ctx.send(response)

@bot.command(name='lol')
async def lol(ctx, nick_tag: str):
    try:
        if '#' not in nick_tag:
            await ctx.send("Por favor senpai, forneça o nome e a tag após o comando (`nick#tag`).")
            return

        nick, tag = nick_tag.split('#', 1)
        puuid, game_name, tag_line = get_user_id(nick, tag)
        match_ids = get_history(puuid)[:5]

        partidas = []
        for match_id in match_ids:
            try:
                match_details = get_game_details(match_id)
                participants = match_details.get('info', {}).get('participants', [])
                for participant in participants:
                    # Acessando estatísticas diretamente do participante
                    stats = {
                        'championName': participant.get('championName'),
                        'kills': participant.get('kills'),
                        'deaths': participant.get('deaths'),
                        'assists': participant.get('assists'),
                    }
                    partidas.append(stats)
            except KeyError as e:
                print(f"Erro ao acessar a chave: {e}")

        response = f"Histórico de partidas de {game_name}#{tag_line}:\n"
        if partidas:
            for match in partidas:
                response += f"Kills: {match.get('kills', 'N/A')}, Mortes: {match.get('deaths', 'N/A')}, Assists: {match.get('assists', 'N/A')}, Champion: {match.get('championName', 'N/A')}\n"
        else:
            response += "Não foram encontradas estatísticas para as partidas."

        await ctx.send(response)
    except Exception as e:
        await ctx.send(f"Desculpe senpai, houve um erro ao buscar as informações: {e}")

@bot.command(name='elo')
async def elo(ctx, nick_tag: str):
    try:
        if '#' not in nick_tag:
            await ctx.send("Formato inválido. Por favor, use o formato `nick#tag`.")
            return

        nick, tag = nick_tag.split('#', 1)
        puuid, game_name, tag_line = get_user_id(nick, tag)
        ranked_data = get_ranked_data(puuid)
        
        if ranked_data:
            response = f"Elo atual de {game_name}#{tag_line}:\n"
            for rank in ranked_data:
                response += f"{rank['queueType']}: {rank['tier']} {rank['rank']} ({rank['leaguePoints']} PDL)\n"
        else:
            response = "Desculpe senpai, não encontrei dados de elo para este invocador."

        await ctx.send(response)
    except Exception as e:
        await ctx.send(f"Desculpe senpai, houve um erro ao buscar os dados de elo: {e}")

bot.run(DISCORD_TOKEN)
