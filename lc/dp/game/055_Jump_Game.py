from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in reversed(range(len(nums))):
            # 从后逐步向前
            # 如果当前位置加上可跳跃数大于等于最后的位置那么更新最后的位置
            if i + nums[i] >= goal:
                goal = i
        return not goal


if __name__ == '__main__':
    s = Solution()
    print(s.canJump([2, 3, 1, 1, 4]))
    print(s.canJump([3, 2, 1, 0, 4]))
