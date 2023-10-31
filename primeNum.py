# take input from user
num = int(input("Enter the number: "))
if num == 1:
    print("it is not prime number.")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print("it is not prime number.")
            break
    else:
        print("it is prime number.")
else:
    print("it is not prime number.")