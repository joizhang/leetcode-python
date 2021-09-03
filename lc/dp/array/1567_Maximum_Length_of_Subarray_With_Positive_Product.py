from typing import List


class Solution:
    """
    https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/discuss/820072/EASY-soultion-with-DRY-RUN-JAVA
    elements      :   9    5    8    2    -6    4    -3    0    2    -5    15    10    -7    9    -2
    positive_len  :   1    2    3    4     0    1     7    0    1     0     1     2     5    6     5
    negative_len  :   0    0    0    0     5    6     2    0    0     2     3     4     3    4     7
    """
    def getMaxLen(self, nums: List[int]) -> int:
        # length of positive and negative results
        positive, negative = 0, 0
        ans = 0
        for num in nums:
            if num == 0:
                positive = 0
                negative = 0
            elif num > 0:
                positive += 1
                negative = 0 if negative == 0 else negative + 1
            else:
                tmp = positive
                positive = 0 if negative == 0 else negative + 1
                negative = tmp + 1
            ans = max(ans, positive)
        return ans

