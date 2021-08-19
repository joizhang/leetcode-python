class Solution:
    def hammingWeight(self, n: int) -> int:
        # 若n&1=0，则n二进制最右一位为0
        # 若n&1=1，则n二进制最右一位为1
        ans = 0
        while n:
            ans += n & 1
            n >>= 1
        return ans
