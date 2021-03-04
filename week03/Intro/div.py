# program that reads in two numbers and outputs the int answer and remainder
# author: Susan Henry

x = int (input("Enter first number: "))
y = int (input("Enter the number you want to divide by: "))
answer = int (x//y)   # // give the int division
remainder = x%y       # % give the remainder

print (" {} divided by {} is {} with remainder {} " .format (x, y, answer, remainder))