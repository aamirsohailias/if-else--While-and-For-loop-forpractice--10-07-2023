# take the list and identify even and odd num
x = [10, 23, 24, 35, 65, 78, 90]
odd = []
even = []
for i in range (len(x)):
    if x[i] % 2 == 0:
        even.append(x[i])
    else:
        odd.append(x[i])
print(even)
print(odd)