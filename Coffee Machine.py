#menu of coffee details
MENU={"expresso":{
    "ingredients":{
    "water":50,
    "coffee":10,
        },
    "cost":1.5,
    },
    "latte":{
    "ingredients":{
    "water":200,
    "milk":150,
    "coffee":24,
        },
    "cost":2.5,
    
        },
    "cappucino":{
    "ingredients":{
    "water":250,
    "milk":100,
    "coffee":24,
        },
    "cost":3.0,
    
        },

    }
profit=0

resources={
    "water":300,
    "milk":200,
    "coffee":100,
    }
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name}")
def is_resource_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item]>=resources[item]:
            print(f"Sorry,there is not enough {item}.")
            return False
    return True
def is_transaction_successful(money_received,cost_of_drink):
    if money_received>=cost_of_drink:
        change=round(money_received-cost_of_drink,2)
        print(f"Here is ${change} in change")
        global profit
        profit+=cost_of_drink
        return True
    else:
        print('Sorry not enough money!')
        return False
def process_coins():
    print('Please Insert the coins: ')
    total=int(input('how many quarters: '))*0.25
    total+=int(input('how many nickles: '))*0.05
    total+=int(input('how many pennies: '))*0.01
    total+=int(input('how many dines: '))*0.1
    return total
is_on=True
while is_on:
    choice=input('What would you like? (expresso/latte/cappucino): ').lower()
    if choice=='off':
        is_on=False
    elif choice=='report':
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money:${profit}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment=process_coins()
            if is_transaction_successful(payment,drink['cost']):
                make_coffee(choice,drink['ingredients'])            










        

