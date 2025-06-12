#BMI Calculator

height=int(input('Enter your Height in Inches: '))

weight=int(input('Enter your Weight in Pounds: '))

bmi=(weight/(height**2))*703

print("Your BMI value is: ",round(bmi,2))

print('You fall under:')

if bmi<18.5:

    print('Underweight category')

elif bmi>18.5 and bmi<24.9:

    print('Normal weight category')

elif bmi>25 and bmi<29.9:

    print('Overweight category')

else:

    print('Obese category 2')

