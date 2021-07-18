class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, ans = 0, 0
        dd = {}
        for i in range(len(s)):
            if s[i] in dd:
                # 出现重复，开始位置加1
                start = max(start, dd[s[i]] + 1)
            ans = max(ans, i - start + 1)
            dd[s[i]] = i
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring(""))
