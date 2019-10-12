import sys

if __name__ == '__main__':
    ## read input
    R, C = map(int, sys.stdin.readline().rstrip().split())
    # read table
    table = [[0] * C for _ in range(R)]
    for i in range(R):
        for j, num in enumerate(map(int, sys.stdin.readline().rstrip().split())):
            table[i][j] = num

    # fill right to left, bottom to up to maximize
    # the outer ring is guranteed to be none zero
    for j in range(C-2, 0, -1):
        for i in range(R-2, 0, -1):
            if not table[i][j]:
                table[i][j] = min(table[i+1][j], table[i][j+1]) - 1

    # check valid
    def valid(i, j, table=table):
        if j + 1 < C:
            if table[i][j] >= table[i][j+1]:
                return False
        if i + 1 < R:
            if table[i][j] >= table[i+1][j]:
                return False
        if j:
            if table[i][j] <= table[i][j-1]:
                return False
        if i:
            if table[i][j] <= table[i-1][j]:
                return False
        return True

    ans = 0
    for j in range(C-1, -1, -1):
        for i in range(R-1, -1, -1):
            if not valid(i, j):
                print(-1)
                exit(0)
            ans += table[i][j]
    print(ans)
