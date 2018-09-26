#Write a program that converts Celsius to Fahrenheit
#09/19/2018
#CTI-110 P2HW1 - Celsius Fahrenheit Converter
#Aria Bodden

#use formula F = 9/5C + 32

#ask user to enter temperature in celsius

Temp_Celsius = int(input('Please enter a temperature in Celsius: '))


#determine formula for temperature in fahrenheit

Temp_Fahr = Temp_Celsius  * (9 / 5) + 32


#show user converted formula (rounded up)

print('The Celsius temperature converted to Fahrenheit is: ' \
      , format(Temp_Fahr, '.0f'))

