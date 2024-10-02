import random

MOTIVATIONAL_PHRASES = [
    "Você não vai se dar por vencido não é, senpai?",
    "Continue, senpai! A vitória está próxima!",
    "Lembre-se, senpai, os desafios são apenas oportunidades disfarçadas!",
    "Não desista, senpai!!! Estou torcendo por você",
]

def get_random_motivation():
    return random.choice(MOTIVATIONAL_PHRASES)