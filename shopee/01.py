#
# Note: 类名、方法名、参数名已经指定，请勿修改
#
#
# 
# @param petals int整型一维数组 花瓣数
# @return int整型
#
class Solution:
    def petalsBreak(self, petals):
        # write code here
        tmp = []
        for petal in petals:
            a, b = petal // 2, petal % 2
            if b == 0:
                tmp.append(a)
            else:
                tmp.append(a + 1)
        return sum(tmp)


if __name__ == '__main__':
    s = Solution()
    print(s.petalsBreak([4, 2, 1]))
    print(s.petalsBreak([2, 3, 10]))
    print(s.petalsBreak([0, 1]))
    print(s.petalsBreak([3, 3, 3, 3]))
