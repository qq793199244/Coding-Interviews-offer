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
    def Find(self, target, array):
        m = len(array)
        n = len(array[0])
        if m == 0 or n == 0:
            return False
        for i in range(m):
            if array[i][-1] < target:
                continue
            left, right = 0, n-1
            while left <= right:
                mid = (left + right) // 2
                if target == array[i][mid]:
                    return True
                elif target < array[i][mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return False


if __name__ == '__main__':
    u = Solution()
    target = 7
    array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    print(u.Find(target, array))