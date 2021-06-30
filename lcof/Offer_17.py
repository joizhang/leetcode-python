from typing import List


class Solution:

    def backtrack(self, n, track, ans):
        if len(track) == n:
            ans.append(''.join(track))
            return

        for i in range(10):
            track.append(str(i))
            self.backtrack(n, track, ans)

    def printNumbers(self, n: int) -> List[int]:
        ans = []
        self.backtrack(n, [], ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.printNumbers(2))
