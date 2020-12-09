'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0
示例1
输入2,3
返回值8.00000
'''
class Solution:
    def Power(self, base, exponent):
        flag = 0
        res = 1
        if base == 0:
            return 0
        if exponent < 0:
            flag = 1
        for i in range(abs(exponent)):
            res = base * res
        if flag == 1:
            res = 1 / res
        return res

if __name__ == '__main__':
    u = Solution()
    base = 2
    exponent = 3
    print(u.Power(base, exponent))