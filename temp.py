from typing import List


class Solution:
    def backtrack(self, nums, visited, track, ans):
        if len(track) == len(nums):
            ans.append(track.copy())
            return

        for i in range(len(nums)):
            if visited[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue
            visited[i] = 1
            track.append(nums[i])
            self.backtrack(nums, visited, track, ans)
            track.pop()
            visited[i] = 0

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited = [0] * len(nums)
        ans = []
        self.backtrack(nums, visited, [], ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1, 1, 2]))
    # print(s.maxLexicographical("1001"))
    # print(s.quick_sort())
    # print(s.insert([[1, 3], [6, 9]], [2, 5]))
