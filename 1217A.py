import sys
from math import floor

if __name__ == '__main__':
    test_case = int(sys.stdin.readline())

    while test_case:
        test_case -= 1

        tmp1, tmp2, tmp3 = sys.stdin.readline().rstrip().split()

        strength, intele, xp = int(tmp1), int(tmp2), int(tmp3)

        strength += xp

        if strength <= intele:
            print(0)
            continue

        ans = min(floor((strength-intele)/2), xp+1)
        if ans != xp+1:
            ans += (1 if (strength-intele)%2 else 0)
        print(ans)
