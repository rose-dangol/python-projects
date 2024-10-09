import random

number=random.randint(1,100)
guess = 0
chance=6

print("Welcome to the Number Guessing Game!")

while(chance!=0):
    guess=int(input("Enter Your Guess:"))

    if(guess<number):
        print("Incorrect, Guess Higher!!")
    elif(guess>number):
        print("Incorrect, Guess Lower!!")
    elif(guess==number):
        print("YAYY, YOU GOT IT!!!")
    chance-=1
    