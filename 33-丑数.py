'''
题目描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
示例1
输入
7
返回值
8
'''


class Solution:
    def GetUglyNumber_Solution(self, index):
        # 牛客网平台上这道题，输入0，输出0
        if index == 0:
            return 0
        dp = [0] * (index + 1)
        dp[1] = 1
        p2, p3, p5 = 1, 1, 1
        for i in range(2, index + 1):
            dp[i] = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
            if dp[i] == dp[p2] * 2:
                p2 += 1
            if dp[i] == dp[p3] * 3:
                p3 += 1
            if dp[i] == dp[p5] * 5:
                p5 += 1
        return dp[index]


if __name__ == '__main__':
    u = Solution()
    print(u.GetUglyNumber_Solution(7))
    print(u.GetUglyNumber_Solution(0))
    print(u.GetUglyNumber_Solution(1))
    print(u.GetUglyNumber_Solution(2))
    print(u.GetUglyNumber_Solution(3))
    print(u.GetUglyNumber_Solution(10))
