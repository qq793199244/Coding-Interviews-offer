'''
题目描述
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
示例1
输入1,2
返回值3
'''

class Solution:
    # 位运算。时间复杂度O(1)，空间复杂度O(1)
    def Add(self, num1, num2):
        MAX = 0x7fffffff
        MASK = 0xffffffff
        while num2:
            num1, num2 = num1 ^ num2, ((num1 & num2) << 1)
            num1 = num1 & MASK
            num2 = num2 & MASK
        return num1 if num1 <= MAX else ~(num1 ^ MASK)



if __name__ == '__main__':
    u = Solution()
    print(u.Add(1, 2))
