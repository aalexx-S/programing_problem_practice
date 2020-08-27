import sys

def main():
    T = int(sys.stdin.readline())
    while T:
        T -= 1

        A = sys.stdin.readline().rstrip()

        X = int(sys.stdin.readline())

        ans = ['0'] * len(A)

        FLAG = True
        # Numbers that have no reference should be zero
        for i in range(len(A) - X, X):
            if A[i] == '1':
                print(-1)
                FLAG = False
                break

        if not FLAG:
            continue

        for i in range(len(A)):
            if not inBound(A, i - X):
                if not inBound(A, i + X):
                    ans[i] = '0'
                else:
                    ans[i] = A[i + X]
                continue

            if not inBound(A, i + X):
                if not inBound(A, i - X):
                    ans[i] = '0'
                else:
                    ans[i] = A[i - X]
                continue

            if A[i - X] == '1' and (not inBound(A, i - (X << 1)) or ans[i - (X << 1)] == '0'):
                ans[i] = '1'
            elif A[i - X] == '0':
                ans[i] = '0'
            else:
                ans[i] = A[i + X]

            if not verify_backward(A, X, i + X, ans):
                print(-1)
                FLAG = False
                break

        if FLAG:
            print(''.join(ans))

def inBound(A, i):
    return 0 <= i < len(A)

def verify_backward(A, X, i, ans):
    #print(f'Verity. len={len(A)}, A[{i}]={A[i]}, ans[{i-X}]={ans[i-X]}, and[{i+X}]={ans[(i+X)%len(A)]}.')
    if ans[i - X] == '1' and A[i] == '0':
        return False
    return True if inBound(A, i + X) else A[i] == ans[i - X]

if __name__ == '__main__':
    main()
