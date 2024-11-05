from typing import Any, str, List, Union


class KMP:
    def __init__(self, pattern: Union[List[Any], str]):
        self.pattern = pattern
        self.n = len(self.s)
        self.kmp = [0] * self.n
        self.build_table()

    def build_table(self):
        for i in range(1, self.n):
            j = self.kmp[i - 1]
            while j > 0 and self.s[i] != self.pattern[j]:
                j = self.kmp[j - 1]

            if self.pattern[i] == self.pattern[j]:
                j += 1
                self.kmp[i] = j

    def search(self, s: Union[List[Any], str]) -> Any:
        m = len(s)
        j = 0
        for i in range(m):
            while j > 0 and s[i] != self.pattern[j]:
                j = self.kmp[j - 1]

            if s[i] == self.pattern[j]:
                j += 1

                if j == self.n:
                    return
