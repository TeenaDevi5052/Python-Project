boolean=True
while boolean:

    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b

    dictionary={
        '+':add,
        '-':sub,
        '*':mul,
        '/':div,
        }
    print('Welcom to the Calculator!')

    op1=int(input('Enter the first number: '))

    op2=int(input('Enter the second number: '))

    op=input('What operation would you like to do? (+ or - or * or /): ')

    if op=='+':
        print(dictionary['+'](op1,op2))
    elif op=='-':
        print(dictionary['-'](op1,op2))
    elif op=='*':
        print(dictionary['*'](op1,op2))
    elif op=='/':
        print(dictionary['/'](op1,op2))
    else:
        print('Invalid input!')

    cont=input('Do you want to continue? (yes or no): ').lower()
    bool_here=True
    while bool_here:
        if cont=='yes':
            boolean=True
            bool_here=False
        elif cont=='no':
            print('Thank you for Visiting!')
            boolean=False
            bool_here=False
        else:
            print('Invalid input.Try Again!')
            bool_here=False
            boolean=True
    
