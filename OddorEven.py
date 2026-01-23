#Check if a input integer is Odd or Even

number = int(input('Enter a number to check whether its even or odd:'))
if number % 2 == 0:
    print('The number entered is even')
else:
    print('The number entered is odd')

#print('The number entered is ' + ('even' if (number := int(input('Enter a number to check whether its even or odd:'))) % 2 == 0 else 'odd'))