import sys

def main():
    # number of cases
    T = int(sys.stdin.readline())
    while T:
        T -= 1

        # read a test case
        N = int(sys.stdin.readline())

        Arr = [int(i) for i in sys.stdin.readline().rstrip()]

        # aggregate array
        agg = [0] * N
        agg[0] = Arr[0]
        for i in range(1, N):
            agg[i] = agg[i-1] + Arr[i]

        # mark next check point
        nxt_zero = [N] * (N + 1)
        nxt_gtone = [N] * (N + 1)
        nxt_gtone[N - 1] = N - 1
        nxt_zero[N - 1] = N - 1
        for i in range(N-2, -1, -1):
            nxt_gtone[i] = i if Arr[i] > 1 else nxt_gtone[i + 1]
            nxt_zero[i] = i if not Arr[i] else nxt_zero[i + 1]

        # test
        ans = 0

        DP = [0] * (N + 1)

        for i in range(N-1, -1, -1):
            j = i if Arr[i] == 1 else nxt_gtone[i]
            while j < N:
                cur = (agg[j] - agg[i - 1] if i else agg[j]) - (j - i + 1)
                if not cur:
                    ans += 1
                    DP[i] += 1

                    # check if continous good sequence
                    if DP[j + 1]:
                        ans += DP[j + 1]
                        DP[i] += DP[j + 1]

                    break

                # jump to next check point
                if cur > 0:
                    if cur <= nxt_gtone[j + 1] - j:
                        j += cur
                    else:
                        j = nxt_zero[j + 1]
                else:
                    j = nxt_gtone[j + 1]

        print(ans)

if __name__ == '__main__':
    main()
