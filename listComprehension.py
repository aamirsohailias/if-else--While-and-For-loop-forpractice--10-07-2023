numbers = [1, 2, 3, 4, 5]
doubled = [(lambda x:x*3)(x) for x in numbers]
print((doubled))