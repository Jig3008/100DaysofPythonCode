print('Welcome to the Roller Coaster!')
height = float(input('What is your height in cm? '))
bill = 0
if height >= 120:
    print('You can ride the roller coaster!')
    age = int(input('Enter your age: '))
    if age >= 18:
        print('Cost without photo is $12')
        bill = 12
    elif age >= 12 and age < 18:
        print('Cost without photo is $7')
        bill = 7
    elif age < 12:
        print('Cost without photo is $5')
        bill = 5
    needsPhoto = input('Do you want a photo as well? Y/N:')
    if needsPhoto == 'Y':
        bill += 3
    print(f'Please pay {bill}')
else:
    print('Sorry, you have to grow taller before you can ride.')