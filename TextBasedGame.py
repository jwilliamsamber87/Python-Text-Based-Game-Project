
rooms = {
    'Home': {'North': 'Tesla', 'South': 'Keller Williams', 'East': 'Chase Bank', 'West': 'Starbucks'},
    'Starbucks': {'East': 'Home'},
    'Keller Williams': {'North': 'Home'},
    'Tesla': {'South': 'Home'}
}


inventory = 0

current_location = rooms['Home']

print('"Welcome and congratulations on deciding to purchase your first home!"')
print('"Your realtor, Mr Brown  has given you a list of items to prepare!"')
print('"He would like to meet at 3 pm to plan your big day!"')
print('"Visit each room and collect your items to prepare for your meeting with Mr. Brown!"')

print('You are Home')

print('You can go move North, East, West, South, or Exit to exit the game!')
player_input = str(input('Enter your move!'))


while current_location == rooms['Home']:
    if player_input != 'Exit' and player_input == 'North':
        current_location = rooms['Tesla']
        print('You are now at Tesla! Item collected!')
        inventory += 1
        player_input = (input('Enter your move!'))

    elif player_input == 'East':
        current_location = rooms['Starbucks']
        print('You are now at Starbucks! Item collected!')
        inventory += 1
        player_input = (input('Enter your move!'))

    elif player_input == 'West':
        current_location = rooms['Chase Bank']
        print('You are now at Chase Bank! Item collected!')
        inventory += 1
        player_input = (input('Enter your move!'))

    elif player_input == 'South':
        current_location = rooms['Keller Williams']
        print('You are now at Keller Williams! item collected')
        inventory += 1
        player_input = (input('Enter your move!'))

while current_location == rooms['Keller Williams']:
    if player_input != 'Exit':
        if player_input == 'North':
            current_location = rooms['Home']
            print('You are now at Home!')
            player_input = (input('Enter your move!'))
            inventory += 1

while current_location == rooms['Starbucks']:
    if player_input != 'Exit':
        if player_input == 'East':
            current_location = rooms['Home']
            print('You are now at Home!')
            player_input = (input('Enter your move!'))
            inventory += 1

        elif player_input == 'Turn in Items!':
            if inventory > 0:
                print('You have visited all rooms and collected all inventory.You won the Game !')

while current_location == rooms['Tesla']:
    if player_input != 'Exit':
        if player_input == 'South':
            current_location = rooms['Home']
            print('You are now at Home!')
            player_input = (input('Enter your move!'))
            inventory += 1

while current_location == rooms['Chase Bank']:
    if player_input != 'Exit':
        if player_input == 'East':
            current_location = rooms['Home']
            print('You are now at Home!')
            player_input = (input('Enter your move!'))
            inventory += 1

else:
    print('Thanks for playing!')



