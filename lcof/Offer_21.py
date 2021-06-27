from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            # 从左往右找偶数
            while lo < hi:
                if nums[lo] % 2 == 0:
                    break
                lo += 1

            while lo < hi:
                if nums[hi] % 2 != 0:
                    break
                hi -= 1

            nums[lo], nums[hi] = nums[hi], nums[lo]
        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.exchange([1,2,3,4]))
