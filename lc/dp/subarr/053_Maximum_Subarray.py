from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        If the sum of a subarray is positive, it has possible to make the next value bigger, so we keep do it until it turn to negative.
        If the sum is negative, it has no use to the next element, so we break.
        it is a game of sum, not the elements.
        """
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)
