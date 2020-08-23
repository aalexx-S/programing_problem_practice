import sys

def main():
    # read number of test cases
    T = int(sys.stdin.readline())
    while T:
        T -= 1

        # read array length
        N = int(sys.stdin.readline())

        # read array
        A = [int(i) for i in sys.stdin.readline().rstrip().split()]

        # pattern match
        # valid pattern: head + non-decreasing slope + top + non-increasing slope + tail.
        # since tail is decided, we can match from tail.
        index = N - 1

        # state 0: matching first slope.
        # state 1: matching second slope.
        state = 0

        while index > 0:
            if state == 0:
                if A[index - 1] >= A[index]:
                    index -= 1
                else:
                    index -= 1
                    state = 1
            if state == 1:
                if A[index - 1] <= A[index]:
                    index -= 1
                else:
                    break

        print(index if index >= 0 else 0)

if __name__ == '__main__':
    main()
