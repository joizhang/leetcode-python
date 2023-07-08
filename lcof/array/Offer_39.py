from typing import List


class Solution:
    """
    剑指 Offer 39. 数组中出现次数超过一半的数字
    """

    # 摩尔投票法：核心理念为票数正负抵消
    def majorityElement(self, nums: List[int]) -> int:
        count, res = 1, nums[0]
        for i in range(1, len(nums)):
            if nums[i] == res:
                count += 1
            else:
                count -= 1

            if count == 0:
                res = nums[i]
                count = 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))
