import sys

if __name__ == '__main__':
    tmp = sys.stdin.readline()
    noq = int(tmp)
    while noq:
        noq -= 1

        ## start of each query
        # read input
        tmp = sys.stdin.readline().split()
        H = int(tmp[0])
        n = int(tmp[1])
        tmp = sys.stdin.readline().split()
        state = 0
        last = 0
        ans = 0
        for i in range(1, n):
            cur = int(tmp[i])
            if not state:
                state = 1
            else:
                if last - cur > 1:
                    ans += 1
                    state = 1
                else:
                    state = 0
            last = cur

        if state and last > 1:
            ans += 1
        print(ans)
