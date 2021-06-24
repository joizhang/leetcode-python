from typing import List


class Solution:

    def backtrace(self, nums: List[int], track: List[int], visited, ans):
        if len(track) == len(nums):
            ans.append(track.copy())
            return

        for i, num in enumerate(nums):
            if visited[i]:
                continue
            # 1 [ , 1, 2] and 1 [1,  , 2] have the same result
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue
            visited[i] = 1
            track.append(num)
            self.backtrace(nums, track, visited, ans)
            del track[-1]
            visited[i] = 0

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) == 0:
            return ans

        nums.sort()
        visited = [0] * len(nums)
        self.backtrace(nums, [], visited, ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1, 2, 3]))
    print(s.permuteUnique([1, 1, 2]))
