class Solution:
    """
    剑指 Offer 48. 最长不含重复字符的子字符串
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        dd = {}
        ans, start = 0, 0
        for i in range(len(s)):
            if s[i] in dd:
                start = max(start, dd.get(s[i]) + 1)
            ans = max(ans, i - start + 1)
            dd[s[i]] = i
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('abcabcbb'))
    print(s.lengthOfLongestSubstring('bbbbb'))
    print(s.lengthOfLongestSubstring('pwwkew'))
    print(s.lengthOfLongestSubstring('au'))
