# using while loop find the factorial of number
# take input from user
num = int(input("Enter the number: "))
fact = 1
i = 1
# implement the while loop in problem
while i <= num:
    fact *= i
    i += 1
# print the output
print("factorial of ", num, " is ", fact)
