class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        ans = 0
        for i in range(2, n + 1):
            ans = (ans + m) % i
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.lastRemaining(5, 3))
    print(s.lastRemaining(5, 1))
    print(s.lastRemaining(10, 17))
