import sys
from math import log2, ceil

if __name__ == '__main__':
    class Seg:
        def __init__(self, l, r, s):
            self.l = l
            self.r = r
            self.rs = ceil((l + r)/2)
            self.leaf_char = 0
            if l < s and l != r:
                self.lst = Seg(self.l, self.rs - 1, s)
                self.rst = Seg(self.rs, self.r, s)

        def update(self, pos, c):
            if self.l == self.r:
                self.leaf_char = 1 << (ord(c) - 97)
                return self.leaf_char

            # go to subtree
            if pos >= self.rs: # right sub tree
                self.leaf_char = self.rst.update(pos, c) | self.lst.leaf_char
            else:
                self.leaf_char = self.lst.update(pos, c) | self.rst.leaf_char
            return self.leaf_char

        def query(self, l, r): # inclusive
            if l == self.l and r == self.r:
                return self.leaf_char

            if bin(self.leaf_char).count('1') == 1:
                return self.leaf_char

            if r < self.rs:
                return self.lst.query(l, r)
            if l >= self.rs:
                return self.rst.query(l, r)
            return self.lst.query(l, self.rs-1) | self.rst.query(self.rs, r)

        def initiate(self, s):
            if self.l > len(s):
                return
            if self.l == self.r:
                self.leaf_char = 1 << (ord(s[self.l-1]) - 97)
                return

            self.lst.initiate(s)
            self.rst.initiate(s)
            self.leaf_char = self.lst.leaf_char | self.rst.leaf_char

    ## read input
    s = sys.stdin.readline().rstrip()
    q = int(sys.stdin.readline())
    # initiate seg tree
    two_pn = pow(2, ceil(log2(len(s))))
    root = Seg(1, int(two_pn), len(s)+1)
    root.initiate(s)
    ## process queries
    lazy = {}
    while q:
        q -= 1
        token = sys.stdin.readline().rstrip().split()
        if token[0] == '1':
            lazy[int(token[1])] = token[2]
        else:
            for i, j in lazy.items():
                root.update(i, j)
            lazy = {}
            print(bin(root.query(int(token[1]), int(token[2]))).count('1'))
