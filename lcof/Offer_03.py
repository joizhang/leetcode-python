from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dd = {}
        for num in nums:
            if num in dd:
                return num
            dd[num] = 1
        return -1

    def findRepeatNumber2(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            num = nums[i]
            if num == i:
                i += 1
                continue
            if num == nums[num]:
                return num
            nums[i], nums[num] = nums[num], nums[i]
            i += 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))
    print(s.findRepeatNumber2([2, 3, 1, 0, 2, 5, 3]))
