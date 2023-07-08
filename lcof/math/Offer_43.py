class Solution:
    """
    剑指 Offer 43. 1～n 整数中 1 出现的次数
    """

    def countDigitOne(self, n: int) -> int:
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high + 1) * digit
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.countDigitOne(12))
    print(s.countDigitOne(13))
