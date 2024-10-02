import requests
from config import RIOT_API_KEY

def get_user_id(nick, tag):
    url = f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{nick}/{tag}?api_key={RIOT_API_KEY}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'Accept-Language': 'pt-BR,pt-PT;q=0.9,pt;q=0.8,en-US;q=0.7,en;q=0.6',
        'Accept-Charset': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://developer.riotgames.com'
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['puuid'], data['gameName'], data['tagLine']

def get_history(puuid):
    url = f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?api_key={RIOT_API_KEY}'
    headers = {'User-Agent': 'Mozilla/5.0', 'Accept-Language': 'pt-BR'}
    response = requests.get(url, headers=headers)
    return response.json()

def get_game_details(match_id):
    url = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={RIOT_API_KEY}'
    headers = {'User-Agent': 'Mozilla/5.0', 'Accept-Language': 'pt-BR'}
    response = requests.get(url, headers=headers)
    return response.json()

def get_ranked_data(summoner_id):
    url = f'https://americas.api.riotgames.com/lol/league/v4/positions/by-summoner/{summoner_id}?api_key={RIOT_API_KEY}'
    headers = {'User-Agent': 'Mozilla/5.0', 'Accept-Language': 'pt-BR'}
    response = requests.get(url, headers=headers)
    return response.json()
