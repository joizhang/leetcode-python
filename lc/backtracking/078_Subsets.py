from typing import List


class Solution:
    """
    数组中的元素 互不相同
    """
    def backtrack(self, nums, start, track, ans):
        ans.append(track.copy())
        for i in range(start, len(nums)):
            track.append(nums[i])
            self.backtrack(nums, i + 1, track, ans)
            track.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        self.backtrack(nums, 0, [], ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3]))
