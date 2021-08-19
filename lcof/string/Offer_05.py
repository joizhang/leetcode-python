class Solution:
    def replaceSpace(self, s: str) -> str:
        if len(s) == 0:
            return s
        return s.replace(' ', '%20')
