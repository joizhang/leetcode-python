import sys

sys.setrecursionlimit(10000000)

N = int(input())
nums = list(map(int, input().split()))
M = sum(nums)


def dfs(nums_, m, pre_tree_class, ans_):
    if m == 0:
        return True
    for i in range(len(nums_)):
        # 当前的树的种类
        tree_class = i + 1
        # 剪枝(某一类大于剩下的坑位一半时就不符合题意了)
        if nums_[i] * 2 > m + 1:
            return False
        if nums_[i] > 0 and pre_tree_class != tree_class:
            nums_[i] -= 1
            ans_.append(tree_class)
            if dfs(nums_, m - 1, tree_class, ans_):
                return True
            ans_.pop()
            nums_[i] += 1
    return False


ans = []
if dfs(nums, M, 0, ans):
    print(' '.join(map(str, ans)))
else:
    print('-')
