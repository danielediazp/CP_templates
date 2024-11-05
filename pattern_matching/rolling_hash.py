from typing import Any, Callable, List, Union

MOD = 2**63 - 1  # Larger input
MOD1 = 10**9 + 7  # Small input


class RollingHash:

    LOWER_ASCII = 31
    ALL_ASCII = 57
    INTS = 0  # Choose the largest int value and offset it by 13

    def __init__(self, s: Union[List[Any] | str], f: Callable[[Any], int]):
        self.s = s
        self.n = len(self.s)
        self.f = f
        self.base = self.LOWER_ASCII
        self.mod = MOD

    def compute_hash(
        self,
        s: Union[List[Any] | str],
    ) -> int:
        h = 0
        for e in s:
            h = (h * self.base + self.f(e)) % self.mod

        return h

    def exec(self, k: int) -> Any:

        rlh = self.compute_hash(self.s[:k])
        p = pow(self.base, k - 1, self.mod)
        for i in range(k, self.n):
            rlh = (rlh - self.f(self.s[i - k]) * p) % self.mod
            rlh = (rlh * self.base + self.f(self.s[i])) % self.mod
