import sys

if __name__ == '__main__':
    ## read input
    q = int(sys.stdin.readline())

    while q:
        q -= 1

        ## read queries
        n = int(sys.stdin.readline())
        pipe = [[], []]
        # read in pipes
        pip_type = {1:1, 2:1, 3:2, 4:2, 5:2, 6:2}
        for i in range(2):
            tmp = map(int, sys.stdin.readline().rstrip())
            pipe[i] = [pip_type[k] for k in tmp]

        ## check accessibility
        # water need to flow to the next cell.
        # water can't flow backward
        state = [1, 0] # water start from (0, 1)
        SUCCESS = True
        for i in range(n):
            if not state[0] and not state[1]:
                SUCCESS = False
                break
            tmp = [0, 0]
            if state[0]:
                tmp[0] = 1 if pipe[0][i] == 1 else 0
                tmp[1] = 1 if pipe[0][i] == 2 and pipe[1][i] == 2 else 0
            if state[1]:
                tmp[1] = 1 if tmp[1] or pipe[1][i] == 1 else 0
                tmp[0] = 1 if tmp[0] or (pipe[0][i] == 2 and pipe[1][i] == 2) else 0
            state = tmp
        # check if water can flow into (1, n+1)
        if SUCCESS and state[1]:
            print("YES")
        else:
            print("NO")
