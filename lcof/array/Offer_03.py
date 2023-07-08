from typing import List


class Solution:
    # 哈希表
    def findRepeatNumber(self, nums: List[int]) -> int:
        dd = {}
        for num in nums:
            if num in dd:
                return num
            dd[num] = 1
        return -1

    # 排序
    def findRepeatNumber2(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]
        return -1

    # 原地交换
    def findRepeatNumber3(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            num = nums[i]
            if num == i:
                i += 1
                continue
            if num == nums[num]:
                return num
            nums[i], nums[num] = nums[num], nums[i]
            # 出错点：不能 +1
            # i += 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))
    print(s.findRepeatNumber([3, 4, 2, 0, 0, 1]))
    print(s.findRepeatNumber2([2, 3, 1, 0, 2, 5, 3]))
    print(s.findRepeatNumber2([3, 4, 2, 0, 0, 1]))
    print(s.findRepeatNumber3([2, 3, 1, 0, 2, 5, 3]))
    print(s.findRepeatNumber3([3, 4, 2, 0, 0, 1]))
