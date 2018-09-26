#Predicting projected sales
#09/24/2018
# CTI-110 P2T1 - Sales Prediction
# Aria Bodden

#ask user to enter projected sales

totalSales = float(input("Enter the projected sales: "))

#calculate the profit at 23% of all sales

profit = totalSales * 0.23

#show projected sales

print("The total profit of projected sales is $ ", format (profit, ",.2f"))


