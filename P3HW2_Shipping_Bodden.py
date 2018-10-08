#Determining shipping rates in relation to package weight
#CTI-110 
# P3HW2 - Shipping Charges 
# Aria Bodden   
# 10/07/2018
#

#prompt user to enter package weight in pounds

weight = float(input("Please enter the weight of the package in pounds: "))

#display rates for weight entered

if weight <=2:
    print("the rate per pound is $1.50")
elif weight <=6:
    print("the rate per pound is $3.00")
elif weight <=10:
    print("the rate per pound is $4.00")
else:
    print("the rate per pound is $4.75")
