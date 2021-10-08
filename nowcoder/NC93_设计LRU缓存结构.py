#
# lru design
# @param operators int整型二维数组 the ops
# @param k int整型 the k
# @return int整型一维数组
#
from collections import OrderedDict


class Solution:
    def __init__(self):
        self.cache = OrderedDict()
        self.capacity = 0

    def set(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def LRU(self, operators, k):
        # write code here
        self.capacity = k
        ans = []
        for operator in operators:
            if len(operator) == 3 and operator[0] == 1:
                self.set(operator[1], operator[2])
            elif len(operator) == 2 and operator[0] == 2:
                ans.append(self.get(operator[1]))
            else:
                continue
        return ans
