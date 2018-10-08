#Debugging program so that it will run correctly
#assigning letter grade to number input
#CTI-110
#Aria Bodden
#P3LAB: Debugging
#10/07/18


def main():
# Assign variables to represent the grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60

#prompt user to enter number grade

    score = float(input('Enter grade: '))

#display results based on entered grade
    if score >= A_score:
        print('Your grade is: A')
    else:
        if score >= B_score:
            print('Your grade is: B')
        else:
            if score >= C_score:
                print('Your grade is: C')
            else:
                if score >= D_score:
                    print('Your grade is: D')
                else:
                    print('Your grade is: F')
main()

