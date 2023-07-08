class Solution:
    """
    剑指 Offer 58 - II. 左旋转字符串
    """

    def reverse(self, s, start, end):
        while start < end:
            tmp = s[start]
            s[start] = s[end]
            s[end] = tmp
            start += 1
            end -= 1

    def reverseLeftWords(self, s: str, n: int) -> str:
        ss = [x for x in s]
        self.reverse(ss, 0, n - 1)
        self.reverse(ss, n, len(s) - 1)
        self.reverse(ss, 0, len(s) - 1)
        return ''.join(ss)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseLeftWords('abcdefg', 2))
