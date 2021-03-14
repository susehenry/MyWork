#program generates random number from 1 to 100 
#asks user to guess number and tells the user if their number is too high or too low
#author: Susan Henry

from random import *  #random numbers info from https://pythonspot.com/random-numbers/

numberToGuess = randint(1, 100)
guess = int(input("Please guess the number:"))
while guess != numberToGuess:

    if guess < numberToGuess:
        print("too low")
        guess = int(input("Please guess again:"))

    else: # cant be equal or too low, so it must be too high
        print("too high")
        guess = int(input("Please guess again:"))

print("Well done! Yes the number was ", numberToGuess)
