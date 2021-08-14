from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = -x
        for num in nums:
            target += num

        if target == 0:
            return len(nums)
        dd, summary, res = {0: -1}, 0, float('-inf')
        for i in range(len(nums)):
            summary += nums[i]
            if summary - target in dd:
                res = max(res, i - dd[summary - target])
            dd[summary] = i
        return len(nums) - res if res != float('-inf') else -1


if __name__ == '__main__':
    s = Solution()
    print(s.minOperations([1, 1, 4, 2, 3], 5))
    print(s.minOperations([5, 6, 7, 8, 9], 4))
    print(s.minOperations([3, 2, 20, 1, 1, 3], 10))
