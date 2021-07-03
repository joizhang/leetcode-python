from typing import List


class Solution:
    def n_sum(self, nums, target, n, index):
        ans = []
        if index > len(nums):
            return ans
        if n == 2:
            i, j = index, len(nums) - 1
            while i < j:
                if nums[i] + nums[j] == target:
                    ans.append([nums[i], nums[j]])
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    j -= 1
        else:
            i = index
            while i < (len(nums) - n + 1):
                temp = self.n_sum(nums, target - nums[i], n - 1, i + 1)
                if temp:
                    for a in temp:
                        b = [nums[i]]
                        b.extend(a)
                        ans.append(b)
                while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                    i += 1
                i += 1
        return ans

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.n_sum(nums, 0, 3, 0)


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
