# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
def EvenOdd():
    num=int(input("Please Enter a Number: "))
    if num%2==0:
        print("Even")
    else:
        print("Odd")
EvenOdd()