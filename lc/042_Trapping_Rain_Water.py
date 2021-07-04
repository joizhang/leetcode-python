from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans, n = 0, len(height)
        if n <= 2:
            return ans
        max_left, max_right = [0] * n, [0] * n
        for i in range(1, n - 1):
            max_left[i] = max(max_left[i - 1], height[i - 1])
        for i in reversed(range(1, n - 1)):
            max_right[i] = max(max_right[i + 1], height[i + 1])

        for i in range(1, n - 1):
            min_height = min(max_left[i], max_right[i])
            if min_height > height[i]:
                ans += (min_height - height[i])

        return ans
