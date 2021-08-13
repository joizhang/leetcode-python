from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i < n:
            while nums[i] - 1 != i:
                tmp = nums[i] - 1
                if nums[i] == nums[tmp]:
                    break
                nums[i], nums[tmp] = nums[tmp], nums[i]
            i += 1

        ans = []
        for i in range(n):
            if nums[i] - 1 != i:
                ans.append(i + 1)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
    print(s.findDisappearedNumbers([1, 1]))
