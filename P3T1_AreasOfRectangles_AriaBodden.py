#Comparing the area of rectangles
#Aria Bodden
# 10/01/18
#P3T1 Areas of Rectangles

#ask user for length and width of first rectangle

RectangleLength1 = float(input("Enter the length of the first rectangle: "))

RectangleWidth1 = float(input("Enter the width of the first rectangle: "))  

#ask user for length and width of second rectangle

RectangleLength2 = float(input("Enter the length of the second rectangle: "))

RectangleWidth2 = float(input("Enter the width of the second rectangle: "))

#formula for calcuating the areas of both rectangles

RecArea1 = RectangleLength1 + RectangleWidth1

RecArea2 = RectangleLength2 + RectangleWidth2

#determine which rectangle has greater area and display results

if RecArea1 > RecArea2:

    print("Rectangle 1 has a greater area than rectangle 2.")

elif RecArea2 > RecArea1:
    print("Rectangle 2 has a greater area than rectangle 1.")

else:
    print("They have the same area.")


