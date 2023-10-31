# armstrong in interval
lower = 100
upper = 2000
# order = len(str(n))
# using for loop
for num in range(lower, upper):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        print(num)