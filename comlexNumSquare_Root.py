# import the module cmath
import cmath
# taken input from user using eval data type
num = eval(input("Enter num: "))
square_root = cmath.sqrt(num)
print("the square of {0} is {1:0.3f}+{2:0.3f}j".format(num, square_root.real, square_root.imag))
