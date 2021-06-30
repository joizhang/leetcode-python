class Solution:
    def numWays(self, n: int) -> int:
        # f(n) = f(n-1) + f(n-2)
        if n == 0:
            return 1
        if n == 1:
            return 1
        memo = [1, 1]
        for i in range(2, n + 1):
            tmp = memo[1]
            memo[1] = (memo[1] + memo[0]) % 1000000007
            memo[0] = tmp
        return memo[1]


if __name__ == '__main__':
    s = Solution()
    print(s.numWays(0))
    print(s.numWays(1))
    print(s.numWays(2))
    print(s.numWays(7))
