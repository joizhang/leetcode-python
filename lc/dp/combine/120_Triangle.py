from typing import List


class Solution:
    """
    we start from the nodes on the bottom row; the min pathsums for
    these nodes are the values of the nodes themselves. From there,
    the min pathsum at the ith node on the kth row would be the
    lesser of the pathsums of its two children plus the value of itself
    """
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [0] * (n + 1)
        for i in reversed(range(n)):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]


if __name__ == '__main__':
    s = Solution()
    print(s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
