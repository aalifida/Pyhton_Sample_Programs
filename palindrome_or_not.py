# Ask the user for a string and print out whether this string is 
# a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
name= input("Enter a number: ")
if name=="".join(reversed(name)):
    print("Palindrome")
else:
    print("Not a Palindrome")
   


    
    
    