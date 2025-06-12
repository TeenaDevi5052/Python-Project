#Who Pays The Bill Randomisation
import random

list_of_friends=['Alice','Bob','Maya','Robert','Peter']

print('In London, Usually the Buissness Professionals catch up occasionally at a Dinner, and after having Dinner\nThey would put all of their Cards at a bowl and pick a Random Card\nThe beholder of the card has to pay the Bill.')

print('\nLet the list be: ' ,list_of_friends)


#either use random.choice(list_of_friends) or

random_number=random.randint(0,4)

print('\n',list_of_friends[random_number],' Has to Pay the Bill')
