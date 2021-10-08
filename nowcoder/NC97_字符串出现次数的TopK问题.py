#
# return topK string
# @param strings string字符串一维数组 strings
# @param k int整型 the k
# @return string字符串二维数组
#
class Solution:
    def topKstrings(self, strings, k):
        # write code here
        dd = {}
        for s in strings:
            if s not in dd:
                dd[s] = 1
            else:
                dd[s] += 1
        ans = []
        

