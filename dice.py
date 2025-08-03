import random as r
inp=input("Role the Dice? (yes or no): ").lower()
while inp=='yes':
    dice = r.randint(1, 6)
    if dice==1:
        print('''    
                  '' '' '' '' '' '' ''
                  ''                ''
                  ''       ()       ''
                  ''                ''
                  '' '' '' '' '' '' ''
                  ''')
    elif dice==2:
        print('''    
              '' '' '' '' '' '' ''
              ''                ''
              ''  ()        ()  ''
              ''                ''
              '' '' '' '' '' '' ''
              ''')
    elif dice==3:
        print('''    
                  '' '' '' '' '' '' ''
                  '' ()             ''
                  ''       ()       ''
                  ''             () ''
                  '' '' '' '' '' '' ''
                  ''')
    elif dice==4:
        print('''    
                  '' '' '' '' '' '' ''
                  '' ()          () ''
                  ''                ''
                  '' ()          () ''
                  '' '' '' '' '' '' ''
                  ''')
    elif dice==5:
        print('''    
                  '' '' '' '' '' '' ''
                  '' ()    ()    () ''
                  ''                ''
                  ''     ()   ()    ''
                  '' '' '' '' '' '' ''
                  ''')
    else:
        print('''    
                  '' '' '' '' '' '' ''
                  '' ()          () ''
                  '' ()          () ''
                  '' ()          () ''
                  '' '' '' '' '' '' ''
                  ''')
    inp2=input('Want to continue? (yes or no): ').lower()
    if inp2=='yes':
        inp='yes'
    else:
        inp='no'
else:
    print('Thank you for visiting!')
