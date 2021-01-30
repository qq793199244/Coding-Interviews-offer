'''
题目描述
统计一个数字在升序数组中出现的次数。
示例1
输入  [1,2,3,3,3,3,4,5],3
返回值 4
'''


class Solution:
    # 暴力法。时间复杂度O(n)，空间复杂度O(1)
    def GetNumberOfK1(self, data, k):
        count = 0
        for d in data:
            if d == k:
                count += 1
        return count

    # 二分查找。时间复杂度O(logn)，空间复杂度O(1)
    def GetNumberOfK2(self, data, k):
        n = len(data)
        if n == 0:
            return 0
        # 找左边界
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if data[mid] < k:
                left = mid + 1
            else:
                right = mid - 1
        bound_l = right
        if left < 0 and data[left] != k:
            return 0
        # 找右边界
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if data[mid] <= k:
                left = mid + 1
            else:
                right = mid - 1
        bound_r = left
        return bound_r - bound_l - 1


if __name__ == '__main__':
    u = Solution()
    data1 = []
    data2 = [1, 2, 3, 3, 3, 3, 4, 5]
    data3 = [1, 2, 3, 3, 3, 3]
    data4 = [1, 1, 1, 1, 1, 2, 3, 4]
    print(u.GetNumberOfK1(data1, 1))
    print(u.GetNumberOfK1(data2, 3))
    print(u.GetNumberOfK1(data3, 3))
    print(u.GetNumberOfK1(data4, 1))

    print(u.GetNumberOfK2(data1, 1))
    print(u.GetNumberOfK2(data2, 3))
    print(u.GetNumberOfK2(data3, 3))
    print(u.GetNumberOfK2(data4, 1))
