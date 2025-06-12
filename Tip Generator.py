#TIP GENERATOR

print('Tip Generator')

cost=float(input('How much does it cost for the order: '))

tip=int(input("How much would you like to tip $10 $20 $30: $"))

customer=int(input('How mamy members are there to divide the bill: '))

tip_as_percent=tip/100

total_tip=cost*tip_as_percent

total_bill=cost+total_tip

bill_per_person=total_bill/customer

final=round(bill_per_person,2)

print(f"Each should pay: ${final}")

