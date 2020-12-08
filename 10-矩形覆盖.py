'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
比如n=3时，2*3的矩形块有3种覆盖方法
'''
class Solution:
    def rectCover(self, number):
        if number <= 2:
            return number
        f1, f2 = 1, 2
        for _ in range(3, number+1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3


if __name__ == '__main__':
    u = Solution()
    print(u.rectCover(1))
    print(u.rectCover(3))
    print(u.rectCover(5))
    print(u.rectCover(10))
    print(u.rectCover(15))
