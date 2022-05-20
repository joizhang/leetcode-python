class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        res = [0] * 26
        for ch in s:
            res[ord(ch) - ord('a')] += 1
