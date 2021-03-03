# converts dollars and cents to the absoloute value of a number
# converts the float number returned  to absolute amount in cent
# author: Susan Henry



number = float (input("Enter a amount in dollars and cents to be debited by the bank: "))
absoluteValue = abs (number)

centAmount = absoluteValue * 100 # there is probably a more accurate formula to convert dollars into cents
roundCent = round (centAmount) # number needs t be rounded to remove decimal

print ('The amount in cent is {} ' . format (roundCent))

