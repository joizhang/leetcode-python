from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        i, j = 0, 1
        while j < len(nums):
            while j < len(nums) and nums[j] == nums[j - 1]:
                j += 1
            if j == len(nums):
                break
            i += 1
            if i != j:
                nums[i] = nums[j]
            j += 1
        return i + 1

    def removeDuplicates2(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        j = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j


if __name__ == '__main__':
    s = Solution()
    a = [1, 1, 2]
    print(s.removeDuplicates(a), a)
    a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(s.removeDuplicates(a), a)
    a = [1, 1]
    print(s.removeDuplicates(a), a)

    a = [1, 1, 2]
    print(s.removeDuplicates2(a), a)
    a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(s.removeDuplicates2(a), a)
    a = [1, 1]
    print(s.removeDuplicates2(a), a)
