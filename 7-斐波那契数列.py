'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项
（从0开始，第0项为0，第1项是1）。
n\leq 39n≤39
示例1
输入4
返回值3
'''
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n <= 1:
            return n
        f0, f1 = 0, 1
        f2 = 0 
        for i in range(2, n+1):
            f2 = f0 + f1
            f0 = f1
            f1 = f2
        return f2 % 1000000007
# 时间复杂度O(n)
# 空间复杂度O(1)

if __name__ == '__main__':
    u = Solution()
    print(u.Fibonacci(0))
    print(u.Fibonacci(1))
    print(u.Fibonacci(2))
    print(u.Fibonacci(4))
    print(u.Fibonacci(5))
    print(u.Fibonacci(10))
    print(u.Fibonacci(100))