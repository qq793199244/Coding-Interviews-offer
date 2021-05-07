'''
题目描述
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
'''


class Solution:
    def __init__(self):
        self.s = []

    def Insert(self, num):
        self.s.append(num)

    def GetMedian(self):
        self.s = sorted(self.s)
        lens = len(self.s)
        if lens == 0:
            return 0
        if lens % 2 != 0:
            return self.s[lens // 2]
        else:
            return (self.s[lens // 2] + self.s[lens // 2 - 1]) / 2.0


if __name__ == '__main__':
    u = Solution()
    u.Insert(2)
    u.Insert(1)
    u.Insert(3)
    u.Insert(4)
    print(u.GetMedian())
    u.Insert(5)
    print(u.GetMedian())
