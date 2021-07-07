#
# Note: 类名、方法名、参数名已经指定，请勿修改
#
#
#
# @param param string字符串
# @return string字符串
#
class Solution:
    def compressString(self, param):
        # write code here
        if len(param) == 0:
            return param
        i = 1
        count = 1
        ans = ''
        while i < len(param):
            if param[i] == param[i - 1]:
                count += 1
            else:
                ans += param[i - 1]
                ans += (str(count) if count > 1 else '')
                count = 1
            i += 1
        ans += param[i - 1]
        ans += (str(count) if count > 1 else '')
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.compressString('aabcccccaaa'))
    print(s.compressString(''))
    print(s.compressString('aaa'))
    print(s.compressString('a'))
    print(s.compressString('b'))
    print(s.compressString('shopeew'))
