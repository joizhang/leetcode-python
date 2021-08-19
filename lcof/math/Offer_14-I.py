class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return 3 ** a
        elif b == 1:
            return (3 ** (a - 1)) * 4
        else:
            return (3 ** a) * 2


if __name__ == '__main__':
    s = Solution()
    print(s.cuttingRope(10))
