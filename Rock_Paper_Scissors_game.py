import random, sys

print('Let us play a game of Rock, Paper, Scissors!')
wins = 0
losses = 0
draws = 0

print('\n')

while True: # The main game loop
    print('You have %s Wins, %s losses, and %s draws ' % (wins, losses, draws))
    while True:   # player input loop
        print('Enter your move: (r) for Rock, (p) for Paper, (s) for Scissors and (q) to Quit')
        playerMove = input()
        if playerMove == 'q' or playerMove=='Q':
            sys.exit()
        if playerMove == 'r' or playerMove== 'p' or player_move=='s':
            break

#Displaying what the player chooses

    if playerMove == 'r':
        print('Rock versus...')
    elif playerMove == 's':
        print('Scissors versus...')
    elif playerMove =='p':
        print('Paper versus...')


    # Computer playing the game
    random_number = random.randint(1,3)
    if random_number ==1:
        computerMove = 'r'
        print('Rock')
    elif random_number==2:
        computerMove = 'p'
        print('Paper')
    elif random_number== 3:
        computerMove = 's'
        print('Scissors')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        print('\n')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        print('\n')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        print('\n')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        print('\n')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        print('\n')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        print('\n')
        losses = losses + 1

