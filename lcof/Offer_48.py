class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        dd = {}
        ans, i = 0, 0
        for j in range(len(s)):
            if s[j] in dd:
                i = max(i, dd.get(s[j]))
            ans = max(ans, j - i + 1)
            dd[s[j]] = j + 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('abcabcbb'))
    print(s.lengthOfLongestSubstring('bbbbb'))
    print(s.lengthOfLongestSubstring('pwwkew'))
    print(s.lengthOfLongestSubstring('au'))
