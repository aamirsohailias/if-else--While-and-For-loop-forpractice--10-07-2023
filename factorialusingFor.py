# find the factorial of number
fact = 1
# taken input from user
num = int(input("Enter the num: "))
# using loop
for i in range (1, num+1):
    fact *= i
print(f"The factorial of {num} is {fact}.")