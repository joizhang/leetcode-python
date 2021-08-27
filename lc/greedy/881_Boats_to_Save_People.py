from typing import List


class Solution:
    """
    https://leetcode-cn.com/problems/boats-to-save-people/solution/gong-shui-san-xie-noxiang-xin-ke-xue-xi-hosg8/
    如果 people[l]+people[r]<=limit，说明两者可以同船，此时船的数量加一，两个指针分别往中间靠拢；
    如果 people[l]+people[r]>limit，说明不能成组，由于题目确保人的重量不会超过 limit 此时让 people[r] 独立成船，船的数量加一，r 指针左移。
    """

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        lo, hi = 0, n - 1
        ans = 0
        while lo <= hi:
            if people[lo] + people[hi] <= limit:
                lo += 1
            hi -= 1
            ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numRescueBoats([1, 2], 3))
    print(s.numRescueBoats([3, 2, 2, 1], 3))
