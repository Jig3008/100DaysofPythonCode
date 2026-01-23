#Bill Calculator Project

print('Welcome to the tip calculator!')
billAmount = float(input('What was the total bill? $'))
tipPercentage = float(input('How much tip would you like to give? 10, 12, or 15? '))
noOfPeople = int(input('How many people to split the bill? '))
perPersonAmount = round((billAmount + ((billAmount * tipPercentage))/100)/noOfPeople,2)
print(f'Each person should pay: ${perPersonAmount}')