import random

random_number = random.randint(1,20)
print('Random number is:', random_number)
print('I am thinking of a number between 1 and 20')

for event in range(6): # has 6 chances to guess
    print('Take a guess')
    guess = int(input())

    if guess < random_number:
        print('your guess is too low')

    elif guess > random_number:
        print('your guess is too high')

    else:
        break       # a correct guess has been made


if  guess == random_number:
    print('Good job! You guessed the number in ' + str(event) + ' guesses')

else:
    print('oops, sorry! Too many tries')
