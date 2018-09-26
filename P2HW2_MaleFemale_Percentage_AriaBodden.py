#display percentages of people in a class
#09/23/2018
#CTI-110 P2HW2 - Male Female Percentage
#Aria Bodden
#I decided to use 46 as my class total instead of 20 for variation

#ask user the total amount of people in the class

Total = int(input('How many people are in your class total?: '))

#ask user how many males are in their class

MaleCount = int(input('How many people in your class are male?: '))

#ask user how many females are in their class

FemaleCount = int(input('How many people in your class are female?: '))

#calculate the number of males in the class

percentage_males = MaleCount / Total

#calculate the number of females in the class

percentage_females = FemaleCount / Total

#show user percentage of females and males in the class

print('The percent is', \

    format(percentage_males, '.0%'), \

      'males and', \

    format(percentage_females, '.0%'), 'females.')

