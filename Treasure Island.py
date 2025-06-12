#Treasure Hunt

#ASCII ART

print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print('Welcome to Treasure Island!')

direction=input("You're at the crossroad Would to like to turn left or right? :").lower()



if direction=='right':
    print('Oh No!.You fell into a Hole!.Game Over')

elif direction=='left':
    
    choice2=input('You have come to a lake. Would you like to Swim or Wait?').lower()
    
    if choice2=='wait':
        
        choice3=input('You arrived at the Island Unharmed, so there are three  doors here.Which one would you wanna choose? (Red,Bule or Yellow)').lower()

        if choice3=='red':
            print('Alas! The room is full of Fire.Game Over!')

        elif choice3=='yellow':
            print('Yay! You Won The Treasure!\nCongratulations on your Win!')

        elif choice3=='blue':
            print('Alas! You were attacked by a bear!')

        else:
            print('Invalid choice!')

    else:
        print('Oh No!,You were attacked by an Alligator.Game Over!')

else:
    print('Invalid Choice!')
