print('Welcome to Treasure Island Quest')
print(''' 
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
directionPath = input('Please choose the right path. Want to go left or right?:')
if directionPath.lower() == 'left':
    swimWait = input('You cleared the first hurdle. Do you want to swim across the river or wait for a boat?:')
    if swimWait.lower() == 'wait':
        print('You now see 3 doors to reach the final treasure')
        choiceDoor = input('Select the door you want to enter? Red/Blue/Yellow:')
        if choiceDoor.lower() == 'red':
            print('You are burned by fire. Game Over!')
        elif choiceDoor.lower() == 'blue':
            print('You are eaten by beasts. Game Over!')
        elif choiceDoor.lower() == 'yellow':
            print('Congratulations! The Treasure is yours. You win!')
        else:
            print('Wrong Choice. Game Over!')
    else:
        print('You are attacked by trout. Game Over!')
    
else:
    print('You fell into a hole. Game Over')