from typing import List


class Solution:
    """
    输入数组可能包含重复元素
    """

    def backtrack(self, nums, start, track, ans):
        ans.append(track.copy())
        for i in range(start, len(nums)):
            if i != start and nums[i] == nums[i - 1]:
                continue
            track.append(nums[i])
            # 出错点：不是start + 1而是i + 1
            self.backtrack(nums, i + 1, track, ans)
            track.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        self.backtrack(nums, 0, [], ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([1, 2, 2]))
    print(s.subsetsWithDup([0]))
