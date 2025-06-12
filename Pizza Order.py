#Pizza Bill Generator

bill=0

size=input('What size of Pizza Do you want? (L or M or S): ')
pepperoni=input('Do you want pepperoni? (Y or N): ')
extra_cheese=input('Do you want Extra Cheese? (Y or N): ')

if size=='L':
    bill+=400
elif size=='M':
    bill+=340
elif size=='S':
    bill+=150
else:
    print('Invalid Input!')

if pepperoni=='Y':
    if size=='L':
        bill+=50
    elif size=='M':
        bill+=35
    else:
        bill+=20
if extra_cheese=='Y':
    bill+=50

print('Your Final Bill: Rs.',bill)
