import random

easy=10
hard=5
guess=0
boolean=True

def compare(guess,number):
        if guess<number:
            return f"{guess} is lower than the actual"
        elif guess>number:
            return f"{guess} is greater than the actual"
        else:
            return "You Guessed it correctly!"

def decide_level(n):
        count=n
        for i in range(0,n):
            guess=int(input('Guess any number: '))
            result=compare(guess,number)
            print(result)
            count-=1
            
            if result=='You Guessed it correctly!':
                print('You Won!')
                break
            print('no.of guess left ',count)
        else:
            print('You lose')
    

while boolean:

    print('Welcome to the number guessing game!')    
    print("I'm thinking of a number between 1 and 100.")
    level=input('Which level do you wanna play?(easy or hard): ').lower()

    number=random.randint(0,100)
    if level=='easy':
        decide_level(10)
        
    elif level=='hard':
        decide_level(5)
        
    else:
        print('Invalid input! Try again.')
        
    if input('Do you want to play again? (yes or no): ').lower()=='yes':
        boolean=True
        
    else:
        print('Thank you for Visiting!')
        boolean=False
            
