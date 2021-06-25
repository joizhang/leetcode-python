from typing import List


class Solution:
    # 可用的左括号数量为left个，可用的右括号数量为rgiht个
    def backtrack(self, left, right, track, ans):
        if left > right:
            return
        if left < 0 or right < 0:
            return
        if left == 0 and right == 0:
            ans.append(''.join(track))
            return

        track.append('(')
        self.backtrack(left - 1, right, track, ans)
        track.pop()

        track.append(')')
        self.backtrack(left, right - 1, track, ans)
        track.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.backtrack(n, n, [], ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
