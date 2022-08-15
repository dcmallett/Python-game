#Python youtube tutorial timestamp: 1:42:32 selecting to print the round results.

from itertools import count
from random import randint


game_running = True

#empty list for our results
game_results = []

def calculate_monster_attack(attack_min, attack_max):
    return randint(attack_min, attack_max)


def game_ends(winner_name):
    print(f'{winner_name} has won the game')

while game_running == True:
    counter = 0
    new_round = True
    player = {'name': 'Dan', 'attack': 10, 'heal': 60, 'health': 100}
    monster = { 'name': 'bob', 'attack_min': 10, 'attack_max': 20, 'health': 100 }

    #this * means we want to print the --- before the start of the game
    print('---' * 7)
    print('Enter player name')
    #allows the user to input a name for the player
    player['name'] = input()

    print(player['name'] + ' has ' + str(player['health']) + ' health')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health')
   
    while new_round == True:
        counter = counter + 1
        player_won = False
        monster_won = False

        print('---' * 7)
        print('Please select an action')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit game')
        print('4) Show the results')

        #input method allows the user to select the input they need to start the game
        player_choice = input()

        #control structers for loops while loops and if statments
        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - calculate_monster_attack(monster['attack_min'], monster['attack_max'])
            if player['health'] <= 0:
                monster_won = True

        elif player_choice == '2':
            player['health'] = player['health'] + player['heal']
            player['health'] = player['health'] - calculate_monster_attack(monster['attack_min'], monster['attack_max'])
            if player['health'] <= 0:
                monster_won = True

        elif player_choice == '3':
            new_round = False
            game_running = False
        
        elif player_choice == '4':
            for result in game_results:
                print(result)
        else: 
            print('Invalid input')
        if player_won == False and monster_won == False:
            print(player['name'] + ' has ' + str(player['health']) + ' left')
            print(monster['name'] + ' has ' + str(monster['health']) + ' left')

        elif player_won:
            game_ends(player['name'])
            round_results = {'name': player['name'], 'health': player['health'], 'Number of rounds': counter}
            game_results.append(round_results)
            new_round = False

        elif monster_won:
            game_ends(monster['name'])
            round_results = {'name': monster['name'], 'health': monster['health'], 'Number of rounds': counter}
            game_results.append(round_results)
            new_round = False