'''
题目描述
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
输入描述:
输入一个字符串,包括数字字母符号,可以为空
返回值描述:
如果是合法的数值表达则返回该数字，否则返回0
示例1
输入"+2147483647"
返回值2147483647
示例2
输入"1a33"
返回值0
'''


class Solution:
    # 时间复杂度O(n)，空间复杂度O(1)
    def StrToInt(self, s):
        res = 0
        s = s.strip()
        if len(s) <= 0:
            return 0
        if s[0] == '+':
            return self.StrToInt(s[1:])
        if s[0] == '-':
            return -self.StrToInt(s[1:])
        for i in range(len(s)):
            if s[i] >= '0' and s[i] <= '9':
                res = res * 10 + int(s[i]) - int('0')
            else:
                return 0
        return res


if __name__ == '__main__':
    u = Solution()
    print(u.StrToInt("+2147483647"))
    print(u.StrToInt("1a33"))
    print(u.StrToInt(" 123"))
