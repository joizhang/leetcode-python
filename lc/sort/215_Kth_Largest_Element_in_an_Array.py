import random
from typing import List


class Solution:
    def partition(self, nums, lo, hi):
        """返回 j 使得 a[lo...j-1] > a[j] > a[j+1...hi]"""
        v = nums[lo]
        i, j = lo + 1, hi
        while True:
            while i <= hi and nums[i] > v:
                i += 1
            while j >= lo + 1 and nums[j] < v:
                j -= 1
            if i > j:
                break
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        nums[lo], nums[j] = nums[j], nums[lo]
        return j

    def findKthLargest(self, nums: List[int], k: int) -> int:
        lo, hi = 0, len(nums) - 1
        p = -1
        while lo <= hi and p + 1 != k:
            p = self.partition(nums, lo, hi)
            if p + 1 < k:
                lo = p + 1
            else:
                hi = p - 1
        return nums[p]

    def quick_sort(self, nums, lo, hi):
        if lo > hi:
            return
        pivot = random.randint(lo, hi)
        nums[lo], nums[pivot] = nums[pivot], nums[lo]
        v = nums[lo]
        # nums[lo+1...i] <= v <= nums[j...hi]
        i, j = lo + 1, hi
        while True:
            while i <= hi and nums[i] < v:
                i += 1
            while j >= lo + 1 and nums[j] > v:
                j -= 1
            if i > j:
                break
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        # 此时nums[i] > v 且 nums[j] < v，所以将lo和v位置的进行交换
        nums[lo], nums[j] = nums[j], nums[lo]
        self.quick_sort(nums, lo, j - 1)
        self.quick_sort(nums, j + 1, hi)

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums[-k]


if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([1, 2, 3, 4, 5, 6], 2))
    print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))
    print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))

    print(s.findKthLargest2([3, 2, 1, 5, 6, 4], 2))
    print(s.findKthLargest2([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
