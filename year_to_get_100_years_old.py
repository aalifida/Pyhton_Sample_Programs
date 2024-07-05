#Create a program that asks the user to enter their name and their age. Print out a message addressed to 
#them that tells them the year that they will turn 100 years old. Note: for this exercise, the expectation 
# is that you explicitly write out the year (and therefore be out of date the next year).
def ageTeller(name: str, age: int):
    current_year=2024
    year_to_100= 100-age+current_year
    print(f"Dear Mr.{name} you will turn 100 years old in {year_to_100}")

name=input("What is your Name:")
age=int(input("What is your current age:"))
ageTeller(name,age)