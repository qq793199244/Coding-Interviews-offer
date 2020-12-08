'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''
class Solution:
    # 递归
    def jumpFloorII(self, number):
        if number <= 1:
            return number
        return 2 * self.jumpFloorII(number - 1) % 1000000007

    # 动态规划优化
    def jumpFloorII2(self, number):
        f1, f2 = 1, 1
        for i in range(2, number+1):
            f2 = 2 * f1
            f1 = f2
        return f2 % 1000000007


if __name__ == '__main__':
    u = Solution()
    print(u.jumpFloorII(1))
    print(u.jumpFloorII2(1))
    print(u.jumpFloorII(2))
    print(u.jumpFloorII2(2))
    print(u.jumpFloorII(3))
    print(u.jumpFloorII2(3))
    print(u.jumpFloorII(4))
    print(u.jumpFloorII2(4))
    print(u.jumpFloorII(5))
    print(u.jumpFloorII2(5))
    print(u.jumpFloorII(10))
    print(u.jumpFloorII2(10))
    print(u.jumpFloorII(50))
    print(u.jumpFloorII2(50))
    print(u.jumpFloorII(100))
    print(u.jumpFloorII2(100))