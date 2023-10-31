# declare lambda function and accepts the larger variable
larger = lambda a, b, c:a if a > b and a > c else(b if b > a and b > c else c)
print(larger(12, 13, 15))