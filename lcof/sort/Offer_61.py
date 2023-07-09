from typing import List


class Solution:
    """剑指 Offer 61. 扑克牌中的顺子"""

    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        joker = 0
        for i in range(4):
            if nums[i] == 0:
                joker += 1
            elif nums[i] == nums[i + 1]:
                return False
        return nums[4] - nums[joker] < 5  # 最大牌 - 最小牌 < 5 则可构成顺子


if __name__ == '__main__':
    s = Solution()
    print(s.isStraight([1, 2, 3, 4, 5]))
    print(s.isStraight([0, 0, 1, 2, 5]))
    print(s.isStraight([11, 8, 12, 8, 10]))
    print(s.isStraight([11, 0, 9, 0, 0]))
