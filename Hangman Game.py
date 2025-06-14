#Hangman Game
import random
print('''

 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       




''')

stages=['''



                    -------------
                     | /       |
                     |/        o
                     |        -+-
                     |         |
                     |        / \                                                                              
                     |
                     |
                 --------------------------


''','''
                     -------------
                     | /       |
                     |/        o
                     |        -+-
                     |         |
                     |        /                                                                              
                     |
                     |
                 --------------------------
''',


        '''

                     -------------
                     | /       |
                     |/        o
                     |        -+-
                     |         |
                     |                                                                                       
                     |
                     |
                 --------------------------


''','''


                     -------------
                     | /       |
                     |/        o
                     |        -+-
                     |
                     |                                                                                 
                     |
                     |
                 --------------------------


''','''

                     -------------
                     | /       |
                     |/        o
                     |        
                     |         
                     |                                                                                 
                     |
                     |
                 --------------------------

''','''

                     -------------
                     | /       |
                     |/        
                     |        
                     |         
                     |                                                                                       
                     |
                     |
                 --------------------------

''','''

                     -------------
                     | /       
                     |/        
                     |        
                     |         
                     |                                                                                     
                     |
                     |
                 --------------------------

''']
word_list=['apple','orange','peach','camel','elephant','panda']

random_word=random.choice(word_list)

correct_letters=[]

game_over=False

lives=6

while not game_over:

    guess=input('Guess a letter:').lower()

    placeholder=''

    for i in range(1,len(random_word)+1):
        placeholder+=' _'
    print(placeholder)

    display=''
    for letter in random_word:
        if letter==guess:
            display+=letter
            correct_letters.append(guess)
            
        elif letter in correct_letters:
            display+=letter
            
        else:
            display+=' _'
    print(display)

    if guess not in random_word:
        lives-=1
        if lives==0:
            game_over=True
            print('You Lose')

    if '_' not in display:
        print('You win')
        game_over=True
    print(stages[lives])
