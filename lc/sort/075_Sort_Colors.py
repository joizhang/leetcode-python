from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        # [0, p0] == 0
        # (p0, p2) = 1
        # [p2, n - 1] == 2
        p0, p2 = -1, n
        i = 0
        while i < p2:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                p2 -= 1
                nums[i], nums[p2] = nums[p2], nums[i]
            else:
                p0 += 1
                nums[i], nums[p0] = nums[p0], nums[i]
                i += 1


if __name__ == '__main__':
    s = Solution()
    a = [2, 0, 2, 1, 1, 0]
    s.sortColors(a)
    print(a)

    a = [2, 0, 1]
    s.sortColors(a)
    print(a)

    a = [0]
    s.sortColors(a)
    print(a)
