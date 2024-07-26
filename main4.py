# https://official-joke-api.appspot.com/random_joke

import requests
import json

def get_random_joke():
    url = 'https://official-joke-api.appspot.com/random_joke'
    response = requests.get(url)
    joke_data = json.loads(response.text)
    print(joke_data)
    print(f"тип: {joke_data['type']}")
    print(f"заголовок: {joke_data['setup']}")
    print(f"панчлайн: {joke_data['punchline']}")

get_random_joke()