import requests
import sys
import os
import csv

def search_pokemon(name):
    #we use GET to get URL
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
    pokemon = response.json()
    print(f"Name: {pokemon['name'].capitalize()}\nID: {pokemon['id']}\nBase XP: {pokemon['base_experience']}")
    
if __name__ == "__main__":
    search_pokemon(sys.argv[1])

    