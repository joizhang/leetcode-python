class Solution:
    def longestPalindrome(self, s: str) -> int:
        dd = {}
        for ch in s:
            if ch not in dd:
                dd[ch] = 1
            else:
                dd[ch] += 1

        ans = 0
        for k, v in dd.items():
            # 字符出现的次数最多用偶数次。
            ans += (v - (v & 1))
        # 如果最终的长度小于原字符串的长度，说明里面某个字符出现了奇数次，
        # 那么那个字符可以放在回文串的中间，所以额外再加一。
        return ans + 1 if ans < len(s) else ans
