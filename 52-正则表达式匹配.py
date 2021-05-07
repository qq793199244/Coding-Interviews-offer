'''
题目描述
请实现一个函数用来匹配包括'.'和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
示例1
输入 "aaa","a*a"
返回值 true
'''


class Solution:
    def match(self, str, pattern):
        # dp问题难就难在状态转移方程！
        m, n = len(str), len(pattern)
        # 状态转移矩阵从0开始，但是0对应字符串是空字符串，所以字符串下标都要加一
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        def match(i, j):
            if i == 0:
                return False
            if pattern[j - 1] == '.':
                return True
            return str[i - 1] == pattern[j - 1]

        dp[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if pattern[j - 1] != '*':
                    if match(i, j):
                        dp[i][j] = dp[i][j] or dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j] or dp[i][j - 2]
                    if match(i, j - 1):
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        return dp[-1][-1]


if __name__ == '__main__':
    u = Solution()
    s1 = "aaa"
    p1 = "a*a"
    print(u.match(s1, p1))  # True

    s2 = "mississippi"
    p2 = "mis*is*p*."
    print(u.match(s2, p2))  # False

    s3 = "ab"
    p3 = ".*"
    print(u.match(s3, p3))  # True
