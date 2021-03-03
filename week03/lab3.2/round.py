# rounds a number
# this program rounds up or down to the nearest number
# e.g 4.5 rounds to 4, but 5.5 rounds to 6
# not recommended to use this when accuarcy is essential

#author:Susan Henry

numberToround = float(input("Enter a float number:"))
roundedNumber = round(numberToround)
print (' {} rounded is {} ' .format(numberToround, roundedNumber))