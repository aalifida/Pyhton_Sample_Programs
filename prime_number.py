# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.). 
#Take this opportunity to practice using functions
import math

def is_prime(n, divisor=2):
    # Base cases
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % divisor == 0:
        return False
    if divisor * divisor > n:
        return True
    # Recursive case
    return is_prime(n, divisor + 1)

print(is_prime(111))
