# swap variables
a = 5
b = 10
# create a temporary variable and swap the values
temp = a
a = b
b = temp
# another way to swapping the variable
a, b = b, a
print("value of a after swapping {}.".format(a))
print("value of b after swapping {}.".format(b))