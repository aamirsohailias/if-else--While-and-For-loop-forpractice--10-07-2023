# import cmath module
import cmath
a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
c = eval(input("Enter c: "))
# using quadratic formula, find the discriminent
d = b **2 -(4*a*c)
sol1 = ((-b + cmath.sqrt(d)) / (2*a))
sol2 = ((-b - cmath.sqrt(d)) / (2*a))
print("The solutions are {0} and {1}".format(sol1, sol2))