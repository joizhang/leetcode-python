class Solution:
    def reverseWords(self, s: str) -> str:
        s_split = s.strip().split()
        lo, hi = 0, len(s_split) - 1
        while lo < hi:
            tmp = s_split[lo]
            s_split[lo] = s_split[hi]
            s_split[hi] = tmp
            lo += 1
            hi -= 1
        return ' '.join(s_split)
