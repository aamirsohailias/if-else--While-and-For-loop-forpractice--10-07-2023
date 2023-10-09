num = int(input("Enter the number: "))
for i in range(1, 10):
    product = num*i
    if i == 7+1:
        break
    print(product, end=' ')