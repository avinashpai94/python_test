import random

randnum = random.randint(1,10)
guess = 0

while randnum != guess:
    guess = int(input("\nEnter a Number"))
    if guess > randnum:
        print("Too high")
    elif guess < randnum:
        print("Too low")
    else:
        print("Correct")