import random

#This would generate a random number between 1 and 10, inclusive
check_random_number = random.randint(1,10)
print(check_random_number)

#This would generate a random floating number between 0 and 1
random_float = random.random()
print(random_float)

#Import a variable from another module
import Import_Module
print(Import_Module.var)

#Heads or Tails
heads_or_Tails = random.randint(0,1)
if heads_or_Tails == 0:
    print('Heads')
else:
    print('Tails')