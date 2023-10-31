# calculate average of lists
average = (lambda *x : sum(x) / len(x) if len(x) > 0 else 0)
result = average(2, 3, 4, 5, 6)
print(result)