'''
题目描述
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
示例1
输入  "abcXYZdef",3
返回值 "XYZdefabc"
'''


class Solution:
    # 时间复杂度O(n)，空间复杂度O(n)
    def LeftRotateString1(self, s, n):
        res = []
        for i in range(n, n + len(s)):
            res.append(s[i % len(s)])
        return ''.join(res)

    # 时间复杂度O(n)，空间复杂度O(n)
    def LeftRotateString2(self, s, n):
        res = ""
        for i in range(n, n + len(s)):
            res += s[i % len(s)]
        return res

    # 时间复杂度O(n)，空间复杂度O(n)
    def LeftRotateString3(self, s, n):
        if not s:
            return s
        n = n % len(s)
        return s[n:] + s[:n]


if __name__ == '__main__':
    u = Solution()
    s1 = ""
    s2 = "abcXYZdef"
    print(u.LeftRotateString1(s1, 3))
    print(u.LeftRotateString1(s2, 3))
    print(u.LeftRotateString1(s2, 12))

    print(u.LeftRotateString2(s1, 3))
    print(u.LeftRotateString2(s2, 3))
    print(u.LeftRotateString2(s2, 12))

    print(u.LeftRotateString3(s1, 3))
    print(u.LeftRotateString3(s2, 3))
    print(u.LeftRotateString3(s2, 12))
