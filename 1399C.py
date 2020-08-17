import sys
from math import floor
from collections import defaultdict

def main():
    # read number of cases
    T = int(sys.stdin.readline())

    while T:
        T -= 1

        # read test case
        N = int(sys.stdin.readline())
        W = sorted([int(i) for i in sys.stdin.readline().strip().split(' ')])

        # aggregate occurence
        WOC = defaultdict(lambda: 0)
        for w in W:
            WOC[w] += 1

        # edge cases
        if N in (0, 1):
            print(0)
            continue
        if N == 2:
            print(1)
            continue

        # iterate possible weights
        ans = 0

        unique_w = list(WOC.keys())

        checked_weight = set()
        for i in range(len(unique_w)):
            for j in range(i, len(unique_w)):
                if i == j and WOC[unique_w[j]] < 2:
                    continue
                s = unique_w[i] + unique_w[j]
                if s in checked_weight:
                    continue
                checked_weight.add(s)

                # check number of combination
                ans = max(ans, comb_chk(s, WOC))

        print(ans)

def comb_chk(s, WOC):
    ret = 0
    W = list(WOC.keys())
    for w in W:
        if w > s/2:
            continue
        cp = s - w
        if cp != w and WOC[cp] > 0:
            ret += min(WOC[w], WOC[cp])

        elif cp == w and WOC[cp] > 1:
            ret += floor(WOC[cp]/2)

    #print(f"comb check: s={s}, comb={ret}.")
    return ret

if __name__ == '__main__':
    main()
