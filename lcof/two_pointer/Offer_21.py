from typing import List


class Solution:

    def exchange(self, nums: List[int]) -> List[int]:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            while lo < hi and nums[lo] % 2 == 1:
                lo += 1
            while lo < hi and nums[hi] % 2 == 0:
                hi -= 1
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1
        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.exchange([2, 1]))
    print(s.exchange([1, 2, 3]))
    print(s.exchange([1, 3, 2]))
    print(s.exchange([3, 2, 1]))
    print(s.exchange([1, 2, 3, 4]))
    print(s.exchange([4, 3, 2, 1]))
    print(s.exchange([1, 3, 2, 4]))
