import random
options = ['R', 'P', 'S',]

def startGame():
    while True:
        print('R for rock, P for paper, S for scissors')
        player_turn = str(input('Pick your option among R or P or S: '))

        if player_turn not in (options):
            print (' ')
            print('Invalid input, please enter a valid input')
            continue

        if player_turn in (options):
            ai_turn = random.choice(options)
            turns = [player_turn, ai_turn]
            text = "Player {} : CPU {} "
            print(text.format(player_turn, ai_turn))

            if player_turn == ai_turn:
                print('Game Tie, start again')
                continue

            if 'R' in turns and 'S' in turns:
                index = turns.index('R')
                if index == 0:
                    print('Player wins')
                if index == 1:
                    print ('Computer wins')
                break

            if 'P' in turns and 'R' in turns:
                index = turns.index('P')
                if index == 0:
                    print('Player wins')
                if index == 1:
                    print ('Computer wins')
                break

            if 'S' in turns and 'P' in turns:
                index = turns.index('S')
                if index == 0:
                    print('Player wins')
                if index == 1:
                    print ('Computer wins')
                break

            else:
                print('An unexpected error occurred, restarting program')
                continue

startGame()