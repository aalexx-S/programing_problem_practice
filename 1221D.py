import sys
from math import ceil

if __name__ == '__main__':
    ## read input
    q = int(sys.stdin.readline())
    while q:
        q -= 1

        ## read query
        F = int(sys.stdin.readline())
        a = [[0, 0] for _ in range(F)]
        for i in range(F):
            a[i][0], a[i][1] = map(int, sys.stdin.readline().rstrip().split())

        ## process query
        dp = [[0, 0, 0] for _ in range(F)]
        dp[0] = [0, a[0][1], 2 * a[0][1]]
        for i in range(1, F):
            diff = a[i][0] - a[i-1][0]
            if diff == 2:
                dp[i][0] = min(dp[i-1][0], dp[i-1][1])
                dp[i][1] = min(dp[i-1]) + a[i][1]
                dp[i][2] = min(dp[i-1]) + 2 * a[i][1]
            elif diff == 1:
                dp[i][0] = min(dp[i-1][0], dp[i-1][2])
                dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + a[i][1]
                dp[i][2] = min(dp[i-1]) + 2 * a[i][1]
            elif diff == 0:
                dp[i][0] = min(dp[i-1][1], dp[i-1][2])
                dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + a[i][1]
                dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + 2 * a[i][1]
            elif diff == -1:
                dp[i][0] = min(dp[i-1])
                dp[i][1] = min(dp[i-1][1], dp[i-1][2]) + a[i][1]
                dp[i][2] = min(dp[i-1][0], dp[i-1][2]) + 2 * a[i][1]
            elif diff == -2:
                dp[i][0] = min(dp[i-1])
                dp[i][1] = min(dp[i-1]) + a[i][1]
                dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + 2 * a[i][1]
            else:
                dp[i][0] = min(dp[i-1])
                dp[i][1] = min(dp[i-1]) + a[i][1]
                dp[i][2] = min(dp[i-1]) + 2 * a[i][1]
        print(min(dp[-1]))
