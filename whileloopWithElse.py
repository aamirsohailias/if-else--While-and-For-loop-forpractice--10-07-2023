num = int(input("enter num: "))
counter = 2
while counter < num:
    if num % counter == 0:
        print("it is not prime number.")
        print(num // counter, "times", counter)
        break
    counter += 1
else:
    print("prime number.")