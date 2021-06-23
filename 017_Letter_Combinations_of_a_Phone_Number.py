from typing import List

d_2_l = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}


class Solution:

    def combine(self, a, letters):
        res = []
        n = len(a)
        if n == 0:
            for l1 in letters:
                res.append(l1)
        else:
            for l1 in a:
                for l2 in letters:
                    res.append(l1 + l2)
        return res

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        for i in digits:
            res = self.combine(res, d_2_l[i])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('234'))
