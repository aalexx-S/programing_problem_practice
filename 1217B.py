import sys
from math import ceil

if __name__ == '__main__':
    test_case = int(sys.stdin.readline())

    while test_case:
        test_case -= 1

        # read in n, x
        n, x = sys.stdin.readline().rstrip().split()
        n, x = int(n), int(x)

        # read in n
        blow = [[0, 0, 0] for _ in range(n)]
        max_d = 0 # max damage after regrow
        final_d = 0 # final blow damage
        for i in range(n):
            tmp1, tmp2 = sys.stdin.readline().rstrip().split()
            blow[i][0], blow[i][1] = int(tmp1), int(tmp2)
            blow[i][2] = blow[i][0] - blow[i][1]
            if blow[i][2] > max_d:
                max_d = blow[i][2]

            if blow[i][0] > final_d:
                final_d = blow[i][0]

        # check if oneshot
        if x <= final_d:
            print(1)
            continue

        # check defeatable
        if max_d <= 0:
            print(-1)
            continue

        print(ceil((x - final_d) / max_d) + 1)
