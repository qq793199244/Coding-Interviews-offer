'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
'''
class Solution:
    def jumpFloor(self, number):
        if number <= 2:
            return number
        f1, f2 = 1, 2
        f3 = 0
        for i in range(3, number+1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3 % 1000000007


if __name__ == '__main__':
    u = Solution()
    print(u.jumpFloor(1))
    print(u.jumpFloor(0))
    print(u.jumpFloor(10))
    print(u.jumpFloor(100))