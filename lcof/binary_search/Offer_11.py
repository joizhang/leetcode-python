from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        lo, hi = 0, len(numbers) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            while lo < mid:
                if numbers[lo] != numbers[hi]:
                    break
                lo += 1
            if numbers[mid] >= numbers[lo] >= numbers[hi]:
                lo = mid + 1
            else:
                hi = mid
        return numbers[lo]
