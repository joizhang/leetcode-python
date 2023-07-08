class Solution:
    """
    剑指 Offer 05. 替换空格
    """

    def replaceSpace(self, s: str) -> str:
        if len(s) == 0:
            return s
        return s.replace(' ', '%20')
