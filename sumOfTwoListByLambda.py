nums = [1,2, 3, 4]
num1 = [2, 3, 4, 5]
square = map(lambda x1, x2 : x1 + x2, nums, num1)
print(list(square))