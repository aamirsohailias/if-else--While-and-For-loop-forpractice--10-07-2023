nterms = int(input("Enter the range: "))
n1, n2 = 0, 1
for i in range(nterms+1):
    print(n1)
    n3 = n1 + n2
    n1, n2 = n2, n3
