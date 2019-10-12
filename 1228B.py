import sys
import itertools

if __name__ == '__main__':
    ## read input
    R, C = map(int, sys.stdin.readline().rstrip().split())
    # read r and c array
    r = list(map(int, sys.stdin.readline().rstrip().split()))
    c = list(map(int, sys.stdin.readline().rstrip().split()))

    ## process fixed cell
    # -1: undecided, 0: white, 1:black
    table = [[-1] * C for _ in range(R)]

    for ind, ri in enumerate(r):
        for k in range(ri):
            table[ind][k] = 1
        if ri < C:
            table[ind][ri] = 0

    # check if impossible
    for ind, ci in enumerate(c):
        for k in range(ci):
            if table[k][ind] == 0:
                print(0)
                exit(0)
            table[k][ind] = 1
        if ci < R:
            if table[ci][ind] == 1:
                print(0)
                exit(0)
            table[ci][ind] = 0

    # count possibility
    free = list(itertools.chain.from_iterable(table)).count(-1)

    print(pow(2, free, (10**9+7)))
