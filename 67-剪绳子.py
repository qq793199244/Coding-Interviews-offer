'''
题目描述
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1，m<=n），每段绳子的长度记为k[1],...,k[m]。
请问k[1]x...xk[m]可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
输入描述:
输入一个数n，意义见题面。（2 <= n <= 60）
返回值描述: 输出答案。
示例1
输入  8
返回值 18
'''


class Solution:
    # 动态规划。时间复杂度O(n^2)，空间复杂度O(n)
    def cutRope(self, number):
        dp = [0 for _ in range(number + 1)]
        dp[1] = dp[2] = 1
        for i in range(3, number + 1):
            for j in range(i):
                dp[i] = max(dp[i], max((i - j) * j, j * dp[i - j]))
        return dp[-1]

    # 动态规划优化。时间复杂度O(n)，空间复杂度O(1s)
    def cutRope2(self, number):
        dp = [0, 1, 1]
        for i in range(3, number + 1):
            dp[i % 3] = max(max(dp[(i - 1) % 3], i - 1),
                            2 * max(dp[(i - 2) % 3], i - 2),
                            3 * max(dp[(i - 3) % 3], i - 3))
        return dp[number % 3]


if __name__ == '__main__':
    u = Solution()
    print(u.cutRope(8))
    print(u.cutRope2(8))
