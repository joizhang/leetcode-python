from typing import List


class Solution:

    def backtrace(self, nums: List[int], track: List[int], visited, ans):
        if len(track) == len(nums):
            ans.append(track.copy())
            return

        for i, num in enumerate(nums):
            if visited[i]:
                continue
            # 当当前元素和前一个元素值相同（此处隐含这个元素的index>0），
            # 并且前一个元素还没有被使用过的时候，我们要剪枝。但实际，
            # 如果条件设为：并且前一个元素被使用过，我们要剪枝，其实也是可以的

            # 例如[1 2 2‘]可能出现[1 2 2'] 和[1 2‘ 2] 的情况 如果
            # “存在前一个相同元素” 且“未被使用过”, 当现有排列是[1 2']时，
            # 原来的数组[1 2 2‘]中2’存在前一个元素2与其相同，且此时2未被访问过，
            # 跳过。[1 2 2']的排列先于[1 2' 2]存在，因此可以去除。
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue
            visited[i] = 1
            track.append(num)
            self.backtrace(nums, track, visited, ans)
            track.pop()
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
