#program that asks a user to input a string and outputs every second letter 
# in reverse order
#author: Susan Henry

#reversing order of letters
secondString = input("Enter a string: ")
print ('Output {}' .format (secondString[::-1]))


#from stack overflow 
#printing out every second letter python

text = input("Message? ")
length = len(text)
for i in range (0, length, 2):
 decoded = text[i]
 
 #print(decoded, end=" ")

 print ('{}' .format (decoded[::-1]))


