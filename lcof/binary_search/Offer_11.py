from typing import List


class Solution:
    """
    剑指 Offer 11. 旋转数组的最小数字
    """
    def minArray(self, numbers: List[int]) -> int:
        lo, hi = 0, len(numbers) - 1
        # 在一个可能存在重复元素值的数组 numbers 寻找旋转点，
        # 旋转点就是最小值
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if numbers[mid] > numbers[hi]:
                lo = mid + 1
            elif numbers[mid] < numbers[hi]:
                hi = mid
            else:
                hi -= 1
        return numbers[lo]


if __name__ == '__main__':
    s = Solution()
    print(s.minArray([3, 4, 5, 1, 2]))
    print(s.minArray([2, 2, 2, 0, 1]))
