#imc
weight = float(input('Enter your weight: '))
height = float(input('Enter your height: '))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print('You are underweight!')
elif 18.5 <= bmi < 25.0:
    print('Congratulations! You are at a healthy weight.')
elif 25.0 <= bmi < 30.0:
    print('You are overweight.')
elif 30.0 <= bmi < 40.0:
    print('You are obese. Please take care of your health!')
elif bmi >= 40.0:
    print('You are morbidly obese. Seek treatment IMMEDIATELY!')
else:
    print('Invalid input. Please make sure to enter correct values for weight and height.')
