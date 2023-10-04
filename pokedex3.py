import requests
import sys
import csv
# pokemon_list = []
# def add_pokemon(name):
#     pokemon_list.append(name)
#     converted_data = add_to_csv(pokemon_list)
#     if len(converted_data) == 6:
#         #print('hello world')
#         pokemon_info(converted_data)
        
# def add_to_csv(pokemon_list):
#     with open('pokemons.csv', 'a', newline='') as pokemon_csv:
#         writer = csv.writer(pokemon_csv)
#         for n in pokemon_list:
#             writer.writerow([n])
            
#     with open('pokemons.csv','r', newline='') as pokemon_file:
#         data = csv.reader(pokemon_file)
#         converted_data =list(data)
        
#     return converted_data

# def pokemon_info(converted_data):
#     new_list = []
#     counter = 0
#     for outer_list in converted_data:
#         for inner_list in outer_list:
#             new_list.append(inner_list)
#             pokemon_name = new_list[counter]
#             response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/")
#             pokemon = response.json()
#             n_items =  pokemon.get('held_items')
#             n_attacks = pokemon.get('moves')
#             n_hp = pokemon.get('stats')[0].get('base_stat')
#             show_pokemon_info(pokemon,n_items,n_attacks,n_hp)
#             counter+=1

# def show_pokemon_info(pokemon,items,attacks,hp):
#         pokemon_attacks = []
#         pokemon_items = []
#         for n in attacks[0:2]:
#             attacks = n['move']['name']
#             pokemon_attacks.append(attacks)
#         for i in items[0:2]:
#             held_items = i['item']['name']
#             pokemon_items.append(held_items)
#         print(f"Name: {pokemon['name'].capitalize()}\nHP:{hp}\nAttacks: {(',').join(pokemon_attacks)}\nHeld items: {(',').join(pokemon_items)}")
#         pokemon_attacks.clear()
#         pokemon_items.clear()
             
# if __name__ == "__main__":
#     add_pokemon(sys.argv[1])
#####################

pokemon_list = []
def add_pokemon(name):
    for p_name in name:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{p_name}/")
        pokemon = response.json()
        n_items = pokemon.get('held_items')
        print(type(n_items))
        n_attacks = pokemon.get('moves')
        n_items = pokemon.get('held_items')
        n_hp = pokemon.get('stats')[0].get('base_stat')
        pokemon_info(pokemon,n_hp,n_attacks,n_items)

def pokemon_info(pokemon,hp,attacks,items):
    pokemon_attacks = [] 
    pokemon_items = []    
    for attack in attacks[0:2]:
        attacks = attack['move']['name']
        pokemon_attacks.append(attacks)
    for item in items[0:2]:
        items = item['item']['name']
        pokemon_items.append(items)
    print(f"Name: {pokemon['name']}\nHP: {hp}\nAttacks: {','.join(pokemon_attacks)}\nHeld items: {','.join(pokemon_items)}\n")
    pokemon_attacks.clear()
    pokemon_items.clear() 
if __name__ == "__main__":
    add_pokemon(sys.argv[1:])
    
#change