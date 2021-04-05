# This program generates 10 random numbers.
# prints them out, then prints out the top 3

#author: Susan Henry


import random

howMany = 10
topHowMany = 3
rangeFrom = 0
rangeto = 100

numbers = []

for i in range(0,10):
 numbers.append(random.randint(rangeFrom,rangeto))
print ("{} random numbers\t {}".format(howMany,numbers))



# https://stackoverflow.com/q/32296887
topOnes = numbers.copy()
topOnes.sort(reverse = True)
print ("The top {} are \t\t {}".format(topHowMany,topOnes[0:topHowMany]))