# taken three sides of triangel from user
a = eval(input("Enter the side1: "))
b = eval(input("Enter the side2: "))
c = eval(input("Enter the side3: "))
s = (a + b + c) / 2
# area of triangle by heron's formula
triangle_Area = (s*(s-a)*(s-b)*(s-c)) **0.5
print(f"The area of triangle is {triangle_Area}.")
print("Area of triangle is %0.2F."%triangle_Area)