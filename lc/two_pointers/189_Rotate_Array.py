from typing import List


class Solution:
    def helper(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        self.helper(nums, 0, n - k - 1)
        self.helper(nums, n - k, n - 1)
        self.helper(nums, 0, n - 1)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(nums, 3)
    print(nums)

    nums = [1, 2, 3, 4, 5, 6]
    s.rotate(nums, 11)
    print(nums)
