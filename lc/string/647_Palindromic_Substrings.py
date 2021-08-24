class Solution:
    def helper(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

    def countSubstrings(self, s: str) -> int:
        """
        类似于最长回文子串
        """
        count = 0
        for i in range(len(s)):
            count += self.helper(s, i, i)
            count += self.helper(s, i, i + 1)
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.countSubstrings('abc'))
    print(s.countSubstrings('aaa'))
