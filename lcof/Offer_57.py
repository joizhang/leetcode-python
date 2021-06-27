from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dd = {}
        for num in nums:
            if target - num in dd:
                return [target - num, num]
            dd[num] = 1
        return [-1, -1]
