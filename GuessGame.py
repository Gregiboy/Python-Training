#Number Guessing game: v0.01
#by Gregory Van Hamme

from random import randint
x = randint(1, 20)
Guess = False

print("Hello, Welcome to the my Number-Guessing game")
print("I am thinking of a number from 1-20")
print("Please take a guess")

while Guess == False:
    myGuess = input()
    if x > myGuess:
        print ("Too Low, take another guess!")
    elif x < myGuess :
        print ("Too High, take another guess!")
    else:
        Guess = True

print ("Nice Guess!")
