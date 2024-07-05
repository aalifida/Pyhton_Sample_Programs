# Take two lists, say for example 
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
# Extras:
# Randomly generate two lists to test this
import random
a = [random.randint(0, 50) for _ in range(20)]
b = [random.randint(0, 50) for _ in range(20)]
print(a, "\n" , b)
new_list = list(set(a) & set(b))
print(new_list)