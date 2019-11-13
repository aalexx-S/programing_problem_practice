import sys

if __name__ == '__main__':
    s = sys.stdin.readline().rstrip()

    if not s:
        print('0')
        exit(0)

    dp = 1
    tra = 0
    if s[0] in ('u', 'n'):
        tra = 1
    if s[0] in ('w', 'm'):
        print(0)
        exit(0)
    prev = s[0]
    ans = 1
    for c in s[1:]:
        if c in ('m', 'w'):
            print(0)
            exit(0)
        if c not in ('u', 'n'):
            tra = 0
            ans = ans * dp % 1000000007
            dp = 1
        if prev != c:
            tra = 1
            ans = ans * dp % 1000000007
            dp = 1
        else:
            # consecutive u or n
            tmp = dp
            dp += tra
            tra = tmp
        prev = c
    print(ans * dp % 1000000007)
