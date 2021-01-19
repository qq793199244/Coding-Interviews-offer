'''
题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
示例1
输入      [[1,2],[3,4]]
返回值     [1,2,4,3]
'''


class Solution:
    # 模拟。时间复杂度O(mn)，空间复杂度O(mn)
    def printMatrix(self, matrix):
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])  # m行，n列
        res = []
        left, right, top, bottom = 0, n - 1, 0, m - 1
        while left <= right and top <= bottom:
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            for i in range(top + 1, bottom + 1):
                res.append(matrix[i][right])
            if left < right and top < bottom:
                for j in range(right - 1, left - 1, -1):
                    res.append(matrix[bottom][j])
                for i in range(bottom - 1, top, -1):
                    res.append(matrix[i][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return res


if __name__ == '__main__':
    u = Solution()
    m1 = []
    m2 = [[1, 2], [3, 4]]
    m3 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    m4 = [[1, 2], [3, 4], [5, 6]]
    print(u.printMatrix(m1))
    print(u.printMatrix(m2))
    print(u.printMatrix(m3))
    print(u.printMatrix(m4))
