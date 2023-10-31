#fibonacci sequence
def fibonacci_sequence(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)
if __name__ == '__main__':
    num = int(input("Enter the num: "))
    print(f"using recursion value of fib({num}) is {fibonacci_sequence(num)}.")
