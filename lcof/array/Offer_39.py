from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes, x, count = 0, nums[0], 0
        for num in nums:
            if votes == 0:
                x = num
            if num == x:
                votes += 1
            else:
                votes -= 1

        for num in nums:
            if num == x:
                count += 1
        return x if count >= len(nums) // 2 else 0
