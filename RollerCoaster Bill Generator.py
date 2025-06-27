#Rollercoaster Bill generator
print('Welcome to the RollerCoaster!')
bill=0
age=int(input('Enter you age: '))
if age>15:    
    print("You're ready to take the RollerCoaster!")    
    if age<=20:       
        bill=200
        print('Actual Amount: ',bill)        
    elif age>20 and age<45:        
        bill=250
        print('Actual Amount is: ',bill)        
    elif age>=45 and age<=55:        
        print('Middle Age Crisis Category\nEnjoy Your Free Tickets!')
    else:
        print('Actual Amount: ',bill)        
    want_photo=input('Would you like to be photographed during your ride? (Yes/No)')
    if want_photo=='Yes' or want_photo=='YES' or want_photo=='yes':        
        bill+=100
        print('Thank you for the confirmation!')        
    print(f"Actual Bill is Rs.{bill}")    
else:    
    print('Underage category\nKindly Enjoy our other rides!')
