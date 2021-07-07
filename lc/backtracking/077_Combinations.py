from typing import List


class Solution:
    def backtrack(self, n, k, start, track, ans):
        if len(track) == k:
            ans.append(track.copy())
            return

        # for i in range(start, n + 1):
        for i in range(start, n - (k - len(track)) + 2):
            track.append(i)
            self.backtrack(n, k, i + 1, track, ans)
            track.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.backtrack(n, k, 1, [], ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
