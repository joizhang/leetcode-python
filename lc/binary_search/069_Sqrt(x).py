class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if mid * mid > x:
                hi = mid - 1
            else:
                lo = mid
        return lo


if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(4))
    print(s.mySqrt(8))
