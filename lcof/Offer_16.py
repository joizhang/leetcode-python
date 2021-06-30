class Solution:

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.
        ans = 1
        if n < 0:
            x, n = 1 / x, -n
        while n:
            if n & 1:
                ans *= x
            x *= x
            n >>= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(2.00000, 10))
    print(s.myPow(2.10000, 3))
    print(s.myPow(2.00000, -2))
