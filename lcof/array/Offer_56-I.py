from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = 0  # 所有数字异或的结果
        a, b = 0, 0
        for n in nums:
            ret ^= n
        # 找到第一位不是0的
        h = 1
        while ret & h == 0:
            h <<= 1
        for n in nums:
            # 根据该位是否为0将其分为两组
            if h & n == 0:
                a ^= n
            else:
                b ^= n
        return [a, b]
