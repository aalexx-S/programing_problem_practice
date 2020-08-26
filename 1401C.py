import sys

def main():
    T = int(sys.stdin.readline())
    while T:
        T -= 1

        N = int(sys.stdin.readline())
        A = [int(i) for i in sys.stdin.readline().rstrip().split()]

        min_element = min(A)

        A_sorted = sorted(A)

        FLAG = True
        for i, j in zip(A, A_sorted):
            if i == j:
                continue

            # Two swap strategies:
            # 1. Directly swap the numbers.
            # 2. Swap the numbers using the min element
            if GCD(j, i) != min_element and (GCD(i, min_element) != min_element or GCD(j, min_element) != min_element):
                FLAG = False
                break

        if FLAG:
            print("YES")
        else:
            print("NO")


def GCD(i, j):
    i, j = max(i, j), min(i, j)

    def __gcd(i, j):
        if j == 0:
            return i
        return __gcd(j, i % j)

    return __gcd(i, j)


if __name__ == '__main__':
    main()
