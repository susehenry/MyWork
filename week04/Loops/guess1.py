#Sentinal controlled loop
#Program to prompt user to guess a number
#will continue to prompt user until correct number is chosen

numberToGuess = 30 #initialise condition variables
guess = int(input("Please guess the number:"))
while guess != numberToGuess:  #check condition
  print ("Wrong")
  guess = int(input("Please guess again:")) #change variables

print ("Well done! Yes the number was ", numberToGuess)
