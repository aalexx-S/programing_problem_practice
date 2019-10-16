import sys
from collections import deque
from itertools import islice

if __name__ == '__main__':
    ## read input
    n, k = map(int, sys.stdin.readline().rstrip().split())
    mes = sys.stdin.readline().rstrip().split()

    ## process
    screen = deque()
    sc_s = set()
    diff_s = set()
    for i in range(k):
        screen.appendleft(i)
        sc_s.add(i)
        diff_s.add(i)
    for m in mes:
        if m not in sc_s:
            sc_s.add(m)
            sc_s.remove(screen.pop())
            screen.appendleft(m)

    sc_s.difference_update(diff_s)

    print(len(sc_s))
    print(' '.join(islice(screen, 0, len(sc_s))))
