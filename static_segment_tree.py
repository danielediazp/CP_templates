from typing import List


class SegmentTree:
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)

        for i in range(self.n):
            self.tree[i + self.n] = arr[i]

        for i in range(self.n - 1, -1, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def query(self, l: int, r: int) -> int:
        l += self.n
        r += self.n

        query = 0
        while l <= r:
            if l % 2:
                query += self.tree[l]
                l += 1

            if not r % 2:
                query += self.tree[r]
                r -= 1

            l //= 2
            r //= 2

        return query

    def update(self, i: int, val: int) -> None:
        i += self.n

        self.tree[i] = val
        while i > 1:
            self.tree[i // 2] = self.tree[i] + self.tree[i ^ 1]
            i //= 2
