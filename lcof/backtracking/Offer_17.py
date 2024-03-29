from typing import List


class Solution:
    nine = 0
    start = 0

    def backtrack(self, n, x, num, ans):
        if x == n:
            s = ''.join(num[self.start:])
            if s != '0':
                ans.append(int(s))
            if n - self.start == self.nine:
                self.start -= 1
            return
        for i in range(10):
            if i == 9:
                self.nine += 1
            num[x] = str(i)
            self.backtrack(n, x + 1, num, ans)
        self.nine -= 1

    def printNumbers(self, n: int) -> List[int]:
        num, ans = ['0'] * n, []
        self.nine, self.start = 0, n - 1
        self.backtrack(n, 0, num, ans)
        return ans


class Solution2:
    def backtrack(self, n, track, ans):
        if n == 0:
            num = int(''.join(track))
            if num != 0:
                ans.append(num)
            return

        for i in range(10):
            track.append(str(i))
            self.backtrack(n - 1, track, ans)
            track.pop()

    def printNumbers(self, n: int) -> List[int]:
        ans = []
        self.backtrack(n, [], ans)
        return ans


if __name__ == '__main__':
    # s = Solution()
    # print(s.printNumbers(2))

    s = Solution2()
    print(s.printNumbers(2))
