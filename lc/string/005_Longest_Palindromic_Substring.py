class Solution:
    def helper(self, s, n, left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        res = ''
        for i in range(n):
            # odd case, like "aba"
            tmp = self.helper(s, n, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, n, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res

    def longestPalindrome2(self, s):
        longest_palindrom = ''
        dp = [[0] * len(s) for _ in range(len(s))]
        # filling out the diagonal by 1
        for i in range(len(s)):
            dp[i][i] = True
            longest_palindrom = s[i]

        # filling the dp table
        for i in range(len(s) - 1, -1, -1):
            # j starts from the i location : to only work on the upper side of the diagonal
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:  # if the chars mathces
                    """
                    # if len slicied sub_string is just one letter if the characters are equal, 
                        we can say they are palindomr dp[i][j] =True 
                    # if the slicied sub_string is longer than 1, then we should check if the 
                        inner string is also palindrom (check dp[i+1][j-1] is True)
                    """
                    if j - i == 1 or dp[i + 1][j - 1] is True:
                        dp[i][j] = True
                        # we also need to keep track of the maximum palindrom sequence
                        if len(longest_palindrom) < len(s[i:j + 1]):
                            longest_palindrom = s[i:j + 1]

        return longest_palindrom


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('babad'))
    print(s.longestPalindrome('cbbd'))
    print(s.longestPalindrome('a'))
    print(s.longestPalindrome('ac'))

    print(s.longestPalindrome2('babad'))
