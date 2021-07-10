'''
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。
示例1
输入 7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
返回值true
'''


class Solution:
    # 按行二分查找。时间复杂度O(mlogn)，空间复杂度O(1)
    def Find(self, target, array):
        if not array or not array[0]:
            return False
        m = len(array)
        n = len(array[0])
        for i in range(m):
            if array[i][-1] < target:
                continue
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if target == array[i][mid]:
                    return True
                elif target < array[i][mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return False

    # 线性查找，类似二叉搜索树（给定的二维数组具备每行从左到右递增以及每列从上到下递增的特点）。
    # 时间复杂度O(m+n)，空间复杂度O(1)
    def Find2(self, target, array):
        if not array or not array[0]:
            return False
        m, n = len(array), len(array[0])
        i, j = m - 1, 0
        while i >= 0 and j <= n - 1:
            if target == array[i][j]:
                return True
            # 若 target > array[i][j]，看同一行的下一列
            elif target > array[i][j]:
                j += 1
            # 若 target < array[i][j]，看同一列的上一行
            else:
                i -= 1
        return False


if __name__ == '__main__':
    u = Solution()
    target = 7
    array1 = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    array2 = []
    array3 = [[], []]
    print(u.Find(target, array1))
    print(u.Find(target, array2))
    print(u.Find(target, array3))
    print('-----------------------')
    print(u.Find2(target, array1))
    print(u.Find2(target, array2))
    print(u.Find2(target, array3))
