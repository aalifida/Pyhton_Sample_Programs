# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.
import random as r
number=int(r.randint(1,10))
count=0
while True:
    count=count+1
    userinput=int(input("Guess the Number between 1 to 10:  "))
    if(number<userinput):
        print("Smaller number please")
    elif(number>userinput):
        print("Greater number please")
    else:
        print(f"Congrats You Guessed the Number:{number} in {count} Attempts")
        break