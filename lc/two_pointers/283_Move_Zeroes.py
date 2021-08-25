from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while True:
            # 找到不为0的
            while j < len(nums) and nums[j] == 0:
                j += 1
            if j == len(nums):
                break
            # 找到为0的
            while i < j and nums[i] != 0:
                i += 1
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1

    def moveZeroes2(self, nums: List[int]) -> None:
            j = 0
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[j] = nums[i]
                    j += 1
            while j < len(nums):
                nums[j] = 0
                j += 1


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    s.moveZeroes(nums)
    print(nums)

    nums = [1, 3, 12, 0, 0]
    s.moveZeroes(nums)
    print(nums)
