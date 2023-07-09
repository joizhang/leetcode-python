class Solution:
    """
    剑指 Offer 50. 第一个只出现一次的字符
    """

    def firstUniqChar(self, s: str) -> str:
        dd = {}
        for c in s:
            if c in dd:
                dd[c] += 1
            else:
                dd[c] = 1
        for k, v in dd.items():
            if v == 1:
                return k
        return " "
