import random

def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    elif sum(cards)>21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user,computer):
    if user==computer:
        return "Draw"
    elif computer==0:
        return "Lost! Opponent has the BlackJack \U0001F62A"
    elif user==0:
        return "Win with a blackJack \U0001F600"
    elif user>21:
        return "Game Over! You Lose. \U0001F62A"
    elif computer>21:
        return "You Win \U0001F600!"
    elif user >computer:
        return "You Win \U0001F600!"
    else:
        return "You Lose! \U0001F62A"
    



    
def play_game():
    game_over=False
    user_cards=[]
    computer_cards=[]
    computer=-1
    user=-1

    for i in range(0,2):
        
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    print('''
                 _     _            _                 _    
                | |   | |          | |  (_)          | |   
                | |__ | | __ _  ___| | ___  __ _  ___| | __
                | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
                | |_) | | (_| | (__|   <| | (_| | (__|   < 
                |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                                       _/ |                
                                      |__/              



    ''')
    while not game_over:

        user=calculate_score(user_cards)
        computer=calculate_score(computer_cards)


        print(f"Your Cards {user_cards}\nCurrent Score: {user}")
        print(f"Computer Cards {computer_cards} \nComputer Score: {computer}")

        if user==0 or computer==0 or user>21:
            game_over=True
        else:
            user_deal=input('Type "y" to get another card and "n" to end the game.\n')
            if user_deal=='y':
                user_cards.append(deal_card())
            else:
                game_over=True

    while computer!=0 and computer<17:
        computer_cards.append(deal_card())
        computer=calculate_score(computer_cards)
        
    print(f"Your final hand is {user_cards}, final score is {user}")
    print(f"Computer final hand is {computer_cards} ,final score is {computer}")
    print(compare(user,computer))
    
while input('Do you want to play the game?(yes or no): ').lower()=='yes':
    print('\n'*50)
    play_game()


    
