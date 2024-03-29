class Solution:
    def findNthDigit(self, n: int) -> int:
        digit, start, count = 1, 1, 9
        while n > count:
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) // digit
        return int(str(num)[(n - 1) % digit])


if __name__ == '__main__':
    s = Solution()
    print(s.findNthDigit(3))
    print(s.findNthDigit(11))
