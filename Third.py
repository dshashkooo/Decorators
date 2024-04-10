import requests
from Fisrt import logger


@logger
def get_the_smartest_superhero(superheroes):
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    heroes_info = requests.get(url).json()

    smartest_superhero = ''
    max_intelligence = 0

    for hero_id in superheroes:
        for hero_info in heroes_info:
            if hero_info['id'] == hero_id:
                intelligence = hero_info.get('powerstats', {}).get('intelligence', 0)
                intelligence = int(intelligence)

                if intelligence > max_intelligence:
                    max_intelligence = intelligence
                    smartest_superhero = hero_info.get('name', 'Unknown')

    return smartest_superhero

# Пример использования
superheroes_list = [1, 2, 3, 4, 5]  # Замените на фактический список id супергероев
smartest_hero = get_the_smartest_superhero(superheroes_list)

print(f"The smartest superhero is: {smartest_hero}")
