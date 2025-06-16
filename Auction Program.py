#AUCTION PROGRAM
print('Welcome to the secret auction program!')
boolean=True

while boolean:

    name=input('Enter you name: ')
    
    bid_amount=int(input('Enter the amount you want to bid: Rs.'))

    new_dict={}
    
    new_dict[name]=bid_amount
    
    other_bidders=input('Are there any other bidders? (Yes or No)').lower()
    
    def find_highest_bid(new_dict):
        max_bid=0
        for i in new_dict:
            if new_dict[i]>0:
                max_bid=new_dict[i]
        print('Highest Bid is: Rs.',max_bid)

    if other_bidders=='yes':
        boolean=True
        print('\n'*100)
        
    elif other_bidders=='no':
        boolean=False
        find_highest_bid(new_dict)
        
    else:
        print('Invalid Input!,Try Again.')
        

