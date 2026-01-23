print('Welcome to Pizza Deliveries!')
size = input('Enter the size of Pizza? S/M/L:')
pepperoni = input('Do you want pepperoni on your pizza? Y/N:')
extra_cheese = input('Do you want extra cheese on your pizza? Y/N:')

total_bill = 0

#Pizza Size
if size == 'L':
    total_bill = 25
elif size == 'M':
    total_bill = 20
else:
    total_bill = 15

#Pepperoni Calc
if pepperoni == 'Y' and (size == 'L' or size == 'M'):
    total_bill += 3
elif pepperoni == 'Y' and size == 'S' :
    total_bill += 2

#Extra Cheese?
if extra_cheese == 'Y':
    total_bill += 1

print(f'Your total bill is {total_bill}')
