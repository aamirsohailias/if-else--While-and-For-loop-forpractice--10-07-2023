# separates types of values from list
n = [23, 'Python',23.98]
x = []
for i in range(len(n)):
    x.append(type(n[i]))
print(x)
print(n)