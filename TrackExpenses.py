#This code is written to track expenses of a person
def add_expense():
    while True:
        try:
            item = input('Enter the item name: (or type "done" to finish:)')
            if item.lower() == 'done':
                break
            else:
                amount = float(input('Enter the amount spent on the item:'))
                with open('expenses.txt','a') as file:
                    file.write(f'{item}: ${amount}\n')
                print(f'{item} added to the expenses file.')
        except ValueError:
            print('Invalid input. Please enter a valid item name.')

def read_expenses():
    with open('expenses.txt','r') as file:
        print(file.read())

#Main function
if(input('Do you want to work with the expenses file? Y/N:').lower() == 'y'):
    add_expense()
    if(input('Do you want to read the expenses file? Y/N:').lower() == 'y'):
        read_expenses()
else:
    print('Exiting the program...')
