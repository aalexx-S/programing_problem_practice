import sys

if __name__ == '__main__':
    ## read input
    q = int(sys.stdin.readline().rstrip())
    while q:
        q -= 1
        ## read case
        n = int(sys.stdin.readline().rstrip())
        room = sys.stdin.readline().rstrip()

        ## process
        # get leftmost and rightmost ladder
        lm = -1
        rm = -1
        for ind, r in enumerate(room):
            if r == '1':
                lm = ind
                break
        for ind, r in enumerate(reversed(room), 1):
            if r == '1':
                rm = len(room) - ind
                break

        if lm == -1 and rm == -1:
            print(n)
        elif lm == rm:
            print(2 * max(lm + 1, n - lm))
        else:
            print(2 * max(rm + 1, n - lm))
