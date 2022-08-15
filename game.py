#Python youtube tutorial timestamp: 

game_running = True

while game_running == True:
    new_round = True
    player = {'name': 'Dan', 'attack': 15, 'heal': 60, 'health': 100}
    monster = { 'name': 'bob', 'attack': 17, 'health': 100 }

    #this * means we want to print the --- before the start of the game
    print('---' * 7)
    print('Enter player name')
    #allows the user to input a name for the player
    player['name'] = input()

    print(player['name'] + ' has ' + str(player['health']) + ' health')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health')
   
    while new_round == True:

        player_won = False
        monster_won = False

        print('---' * 7)
        print('Please select an action')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit game')

        #input method allows the user to select the input they need to start the game
        player_choice = input()

        #control structers for loops while loops and if statments
        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - monster['attack']
            if player['health'] <= 0:
                monster_won = True

        elif player_choice == '2':
            player['health'] = player['health'] + player['heal']
            player['health'] = player['health'] - monster['attack']
            if player['health'] <= 0:
                monster_won = True

        elif player_choice == '3':
            new_round = False
            game_running = False
        else: 
            print('Invalid input')
        if player_won == False and monster_won == False:
            print(player['name'] + ' has ' + str(player['health']) + ' left')
            print(monster['name'] + ' has ' + str(monster['health']) + ' left')

        elif player_won:
            print(player['name'] + ' won')
            new_round = False

        elif monster_won:
            print('The monster won')
            new_round = False
