from typing import List


class Solution:
    def backtrack(self, candidates, target, start, track, ans):
        if target < 0:
            return
        if target == 0:
            ans.append(track.copy())
            return
        for i in range(start, len(candidates)):
            if target < candidates[start]:
                break
            track.append(candidates[i])
            self.backtrack(candidates, target - candidates[i], i, track, ans)
            track.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.backtrack(candidates, target, 0, [], ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))
    print(s.combinationSum([2, 3, 5], 8))
