#This code is to play a game of Rock papers and scissors between User and Computer
import random

def checkWinner(compChoice, userChoice, choiceSet):
    compIndex = choiceSet.index(compChoice)
    if compIndex == userChoice:
        print('Game ends in draw!')
    elif (userChoice == 0 and compIndex == 2) or (userChoice == 2 and compIndex == 1) \
        or (userChoice == 2 and compIndex == 1):
        print('Congratulations you win!')
    else:
        print('You lose!')

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

choicesList = [rock, paper, scissor]
userInput = int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor:'))
print(choicesList[userInput])
computerChoice = random.choice(choicesList)
print('Computer chooses')
print(computerChoice)

checkWinner(computerChoice, userInput, choicesList)

