from random import randint
import sys

number = randint(0, 100)

while True:
    print(number)
    guess = input("Which number is your guess? (range 0-100)")
    if int(guess) > number:
        print("The number is smaller!")
    elif int(guess) < number:
        print("The number is bigger!")
    else:
        print("Congratulations! You guessed it!")
        break


