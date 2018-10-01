#ask user to enter weight

weight = float(input("Please enter your weight: "))

#ask user to enter height

height = float(input("Please enter your height: "))

#assign variable for weight formula

BMI = weight * 703 / height**2

#display BMI

print("Your BMI is: ", format(BMI, ',.2f'))

#determine if person is optimal, overweight, or underweight

if BMI < 18.5:
    print("you are underweight.")

elif BMI > 25:
    print("YOu are overweight.")

else:
    print("You are the optimal weight.")
