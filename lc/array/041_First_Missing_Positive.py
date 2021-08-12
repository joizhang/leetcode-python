from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i] != i + 1:
                if nums[i] <= 0 or nums[i] >= n + 1 or nums[i] == nums[nums[i] - 1]:
                    break
                idx = nums[i] - 1
                nums[i] = nums[idx]
                nums[idx] = idx + 1

        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1


if __name__ == '__main__':
    s = Solution()
    print(s.firstMissingPositive([1, 2, 0]))
    print(s.firstMissingPositive([3, 4, -1, 1]))
    print(s.firstMissingPositive([7, 8, 9, 11, 12]))
