#Rock Paper Scissors
import random

inputs=input('Welcome To the Game!\nChoose Rock ,Paper or Scissors: ').lower()

rock=('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

''')
paper=('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

''')
scissors=('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

random_integer=random.randint(1,3)

if inputs=='rock':
    
    print(rock,'\n You chose Rock.')
    if random_integer == 1:
        
        print(rock,'\nComputer chose Rock!\nMatch draw. ')
    elif random_integer == 2:
        print(paper,'\nComputer chose Paper!\nComputer Won!')
    else:
        print(scissors,'\nComputer chose Scissors!\nYou Won the Game!')

        
elif inputs=='paper':
   
    print(paper,'You chose Paper.')
    if random_integer == 1:
        print(rock,'\nComputer chose Rock!\nYou Won the Game!. ')
    elif random_integer == 2:
        print(paper,'\nComputer chose Paper!\nMatch draw.')
    else:
        print(scissors,'\nComputer chose Scissors!\nComputer Won.')

        
elif inputs=='scissors':
   
    print(scissors,'You chose Scissors.')
    if random_integer == 1:
        print(rock,'\nComputer chose Rock!\nComputer Won! ')
    elif random_integer == 2:
        print(paper,'\nComputer chose Paper!\nYou Won the Game!')
    else:
        print(scissors,'\nComputer chose Scissors!\nMatch draw.')

        
else:
    print('Invalid Input!')


