def nqueens(n):
    left = set()
    upper = set()
    lower = set()
    
    board = [["0"] * n for i in range(n)]
    res = []
    def backtrack(col):
        if col == n:
            copy = [" ".join(row) for row in board]
            res.append(copy)
            return
        for row in range(n):
            if row in left or (row + col) in lower or (n - 1 + col - row) in upper:
                continue
            
            board[row][col] = "1"
            left.add(row)
            lower.add(row+ col)
            upper.add(n - 1 + col - row)
            
            backtrack(col + 1)
            
            board[row][col] = "0"
            left.remove(row)
            lower.remove(row + col)
            upper.remove(n - 1 + col - row)
    backtrack(0)
    count = 0
    for sol in res:
        for row in sol:
            print(row, " ")
        print()
        count += 1
    print(count)

if __name__ == "__main__":
    n = int(input("Enter the number of queens: "))
    nqueens(n)
