#BMI Calculator
# Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.
# If the bmi is under 18.5 (not including), print out "underweight"
# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
# If the bmi is 25 (including) or over, print out "overweight"

height = float(input('Enter your height in inches:'))
weight = float(input('Enter your weight in kgs:'))

bmi = weight/(height ** 2)

print(f'Your BMI is {bmi}')

if bmi < 18.5:
    print(f'Your BMI is {bmi}. You are underweight')
elif bmi >= 18.5 and bmi < 25:
    print(f'Your BMI is {bmi}. You have normal weight')    
else:
    print(f'Your BMI is {bmi}. You are overweight')