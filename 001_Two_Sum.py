from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dd = {}
        for i, num in enumerate(nums):
            if target - nums[i] in dd:
                return [dd[target - nums[i]], i]
            dd[nums[i]] = i


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
    print(s.twoSum([3, 2, 4], 6))
    print(s.twoSum([3, 3], 6))
