from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        days_idx = 0  # 出行日期索引
        for i in range(1, days[-1] + 1):
            if i != days[days_idx]:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[max(0, i - 1)] + costs[0],
                            dp[max(0, i - 7)] + costs[1],
                            dp[max(0, i - 30)] + costs[2])
                days_idx += 1
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))
    print(s.mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]))
