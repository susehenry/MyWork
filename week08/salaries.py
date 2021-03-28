# Lab week 08
#Program makes a list of 10 random salaries
#author:Susan henry


import numpy as np


minSalary= 20000 #set parameters at beginning of program
maxSalary = 80000
numberOfEntries = 10
np.random.seed(1) #prints same random numbers each time

salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)
salariesPlus = salaries + 5000 # adds 5000 to each value
salariesMult = salaries * 1.05 # add 5% by multiplying by 1.05
newSalaries = salariesMult.astype(int)



print (salaries)
print (salariesPlus)
print(salariesMult)
print(newSalaries)