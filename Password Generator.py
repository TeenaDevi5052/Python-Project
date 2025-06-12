import random
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','4','3','5','6','7','8','9','0']
characters=['!','@','#','+','(',')','&','*','%']

print('Welcome to Password Generator')
my_letters=int(input('How many letters would you like to have in your Password?\n'))
my_symbols=int(input('How many symbols would you like to have in your Password?\n'))
my_numbers=int(input('How many numbers would you like to have in your Password?\n'))


password=[]

for i in range(1,my_letters+1):
    password.append(random.choice(alphabets))


for j in range(1,my_symbols+1):
    password.append(random.choice(numbers))


for k in range(1,my_numbers+1):
    password.append(random.choice(characters))

#before shuffle
#random
random.shuffle(password)
new_password=''
for i in password:
    new_password+=i
print('Your Password is:' ,new_password)
