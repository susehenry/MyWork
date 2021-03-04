# User inputs a range of numbers
# Program prints out random number from the specified range
# author: Susan Henry

import random

x = int (input("Enter first number: "))
y = int (input("Enter second number: "))

number = random.randint (x, y)
print ("Here is a random number {}" .format (number))
