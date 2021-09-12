import random

secret_number = random.randint(1,10)

guess = int(input("Guess the number between 1 and 10: "))

if (guess  == secret_number):
    print ("Player wins and computer loses")
else:
    print ("Player loses and computer wins")

