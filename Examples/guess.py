"""
This uses the random module: https://www.w3schools.com/python/module_random.asp

Exercises:
1. Can you make it a number between one and 100? Give more hints depending on whether the player is close or not? And change the number of guesses that the player can make?
2. Can you make the game into a function called startgame(difficulty) which starts a game and accepts the game difficulty as a parameter?
3. What do {0} and {1} do in the final lines of the program? How else could you write this?
4. How would you go about adding a computer opponent which also takes turns guessing?

"""

import random

guesses_made = 0

name = input('Hello! What is your name?\n')
number = random.randint(1, 20)
print ('Well, ' + name + ', I am thinking of a number between 1 and 20 (inclusive).')

while guesses_made < 6:

    guess = int(input('Take a guess: '))

    guesses_made += 1

    if guess < number:
        print ('Your guess is too low.')

    if guess > number:
        print ('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    print ('Good job, {0}! You guessed my number in {1} guesses!'.format(name, guesses_made))
else:
    print ('Nope. The number I was thinking of was {0}'.format(number))