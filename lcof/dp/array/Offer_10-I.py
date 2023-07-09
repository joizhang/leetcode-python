class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        memo = [0, 1]
        i = 2
        while i <= n:
            x = (memo[0] + memo[1]) % 1000000007
            memo[0] = memo[1]
            memo[1] = x
            i += 1
        return memo[1]


if __name__ == '__main__':
    s = Solution()
    print(s.fib(5))
