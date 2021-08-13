from typing import List


class Solution:
    def dfs(self, n, cur, ans):
        if cur > n:
            return
        ans.append(cur)
        for i in range(10):
            if 10 * cur + i > n:
                return
            self.dfs(n, 10 * cur + i, ans)

    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        for i in range(1, 10):
            self.dfs(n, i, ans)
        return ans
