# calcuate a persons body mass index
# author: Susan Henry

#input persons weight in kilograms and height in cms
weight = float (input ('Enter weight in kg:'))
height = float (input ('Enter height in cms:'))

#calcution for bmi 
bmi = round (weight / (height/100 * height/100), 2)

# Display the result
print ('Your BMI is: {}'. format (bmi) )