def fib_recursive(n):
    if n <= 1:
        return n;
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

if __name__ == "__main__":
    n = input("Enter the number :")
    n = int(n)
    for i in range(n):
        print(fib_recursive(i))
