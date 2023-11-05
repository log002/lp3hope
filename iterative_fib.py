def fib_iterative(n):
    first = 0
    second = 1
    print(first)
    print(second)
    while n - 2 > 0:
        third = first + second
        print(third)
        first = second
        second = third
        n -= 1
if __name__ == "__main__":
    n = input("Enter the value of n: ")
    n = int(n)
    fib_iterative(n)
