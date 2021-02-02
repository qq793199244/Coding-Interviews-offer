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

    def LeftRotateString4(self, s, n):
        '''
        假设字符串abcdef，n=3，
        设X=abc，Y=def，所以字符串可以表示成XY，问如何求得YX。
        假设X的翻转为XT，XT=cba，
        同理YT=fed，那么YX=(XTYT)T
        '''
        s_len = len(s)
        if s_len == 0 or n % s_len == 0:
            return s

        def reverse(str, begin, end):
            while begin <= end:
                str[begin], str[end] = str[end], str[begin]
                begin += 1
                end -= 1
            return str

        s = list(s)
        reverse(s, 0, (n - 1) % s_len)
        reverse(s, n % s_len, s_len - 1)
        reverse(s, 0, s_len - 1)
        return ''.join(s)


if __name__ == '__main__':
    u = Solution()
    s1 = ""
    s2 = "abcXYZdef"
    print(u.LeftRotateString1(s1, 3))
    print(u.LeftRotateString1(s2, 3))
    print(u.LeftRotateString1(s2, 12))
    print(u.LeftRotateString1(s2, 0))

    print(u.LeftRotateString2(s1, 3))
    print(u.LeftRotateString2(s2, 3))
    print(u.LeftRotateString2(s2, 12))
    print(u.LeftRotateString2(s2, 0))

    print(u.LeftRotateString3(s1, 3))
    print(u.LeftRotateString3(s2, 3))
    print(u.LeftRotateString3(s2, 12))
    print(u.LeftRotateString3(s2, 0))

    print(u.LeftRotateString4(s1, 3))
    print(u.LeftRotateString4(s2, 3))
    print(u.LeftRotateString4(s2, 12))
    print(u.LeftRotateString4(s2, 0))
