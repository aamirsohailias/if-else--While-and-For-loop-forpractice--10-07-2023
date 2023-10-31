# declare variable with list
numbers = [2, 3, 4, 5, 6]
squared = []
# using lambda function
square = lambda n: n**2
# using for loop iterable the items of list
for i in numbers:
    # using append function to squared each element of list
    squared.append(square(i))
# taken output
print(squared)