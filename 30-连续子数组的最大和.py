'''
题目描述
输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。
求所有子数组的和的最大值。要求时间复杂度为 O(n).
示例1
输入
[1,-2,3,10,-4,7,2,-5]
返回值
18
'''


class Solution:
    # 贪心法。时间复杂度O(n) 空间复杂度O(1)
    def FindGreatestSumOfSubArray(self, array):
        n = len(array)
        if n == 0:
            return 0
        tmp = 0
        max_sum = array[0]
        for i in range(n):
            if tmp < 0:
                tmp = 0
            tmp += array[i]
            max_sum = max(max_sum, tmp)
        return max_sum


if __name__ == '__main__':
    u = Solution()
    a1 = [1, -2, 3, 10, -4, 7, 2, -5]
    print(u.FindGreatestSumOfSubArray(a1))
