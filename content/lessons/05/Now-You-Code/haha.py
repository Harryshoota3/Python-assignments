from random import *

def guess():
    number = randint(1,100)
    i = 0
    print("I am thinking of a number between 1 and 100...")
    while True:
        guess = int(input("You guess:"))
        if guess > number:
            print("Too high, Guess lower.")
            i +=1
        elif guess < number:
            print("Too low, Guess higher.")
        elif guess == number:
            i +=1
            print("You guessed it in",i,"tries.")
            break

guess()
