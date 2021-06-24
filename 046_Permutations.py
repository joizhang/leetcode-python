from typing import List


class Solution:

    def backtrace(self, nums: List[int], track: List[int], ans):
        if len(track) == len(nums):
            ans.append(track.copy())
            return

        for num in nums:
            if num in track:
                continue
            track.append(num)
            self.backtrace(nums, track, ans)
            del track[-1]

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backtrace(nums, [], ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
    print(s.permute([0,1]))
