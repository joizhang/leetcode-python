from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == '__main__':
    s = Solution()
    a = [3, 2, 2, 3]
    s.removeElement(a, 3)
    print(a)
