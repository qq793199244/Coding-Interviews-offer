'''
题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
返回值描述:
对应每个测试案例，输出两个数，小的先输出。
示例1
输入  [1,2,4,7,11,15],15
返回值     [4,11]
'''


class Solution:
    # 在LeetCode超时。时间复杂度O(n^2)，空间复杂度O(1)
    def FindNumbersWithSum(self, array, tsum):
        for i in array:
            if tsum - i in array:
                return [i, tsum - i]
        return []


    # 双指针。时间复杂度O(n)，空间复杂度O(1)
    def FindNumbersWithSum2(self, array, tsum):
        n = len(array)
        i, j = 0, n-1
        while i < j:
            s = array[i] + array[j]
            if s > tsum:
                j -= 1
            elif s < tsum:
                i += 1
            else:
                return [array[i], array[j]]
        return []


if __name__ == '__main__':
    u = Solution()
    array1 = [1, 2, 4, 7, 11, 15]
    print(u.FindNumbersWithSum(array1, 15))
    print(u.FindNumbersWithSum2(array1, 15))
