# recursive

def fabonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fabonacci_recursive(n-1) + fabonacci_recursive(n-2)
if __name__ == "__main__":
    n = input("Enter the number :")
    n=int(n)
    for i in range(n):
        print(fabonacci_recursive(i))
