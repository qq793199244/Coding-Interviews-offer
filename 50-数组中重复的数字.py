'''
题目描述
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中第一个重复的数字。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
返回描述：
如果数组中有重复的数字，函数返回true，否则返回false。
如果数组中有重复的数字，把重复的数字放到参数duplication[0]中。（ps:duplication已经初始化，可以直接赋值使用。）
'''


class Solution:
    def duplicate(self, numbers, duplication):
        n = len(numbers)
        if n == 0:
            duplication[0] = -1  # 不加这句也能过
            return False
        d = {}
        for num in numbers:
            d[num] = d.get(num, 0) + 1
        for num in numbers:
            if d[num] > 1:
                duplication[0] = num
                return True
            else:
                duplication[0] = -1  # 不加这句也能过
        return False


'''
牛客网更新
'''
#题目描述
# 在一个长度为n的数组里的所有数字都在0到n-1的范围内。
# 数组中某些数字是重复的，但不知道有几个数字是重复的。
# 也不知道每个数字重复几次。请找出数组中任一一个重复的数字。
# 例如，如果输入长度为7的数组[2,3,1,0,2,5,3]，那么对应的输出是2或者3。存在不合法的输入的话输出-1
# 输入 [2,3,1,0,2,5,3]
# 返回值 2或3

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# @param numbers int整型一维数组
# @return int整型
#
class Solution1:
    def duplicate(self, numbers):
        # write code here
        n = len(numbers)
        if n == 0 or n == 1:
            return -1
        d = {}
        for num in numbers:
            d[num] = d.get(num, 0) + 1
        for num in numbers:
            if d[num] > 1:
                return num
        return -1


if __name__ == '__main__':
    u = Solution()
    duplication = [None]
    nums1 = [2, 3, 1, 0, 2, 5, 3]
    nums2 = [1, 1, 1, 1, 1, 1]
    nums3 = []
    nums4 = [1, 2, 3, 4]
    nums5 = [1, 0, 1, 0, 2, 3, 4]
    nums6 = [2, 1, 3, 0, 4]
    print(u.duplicate(nums1, duplication), "| duplication[0]=", duplication[0])
    print(u.duplicate(nums2, duplication), "| duplication[0]=", duplication[0])
    print(u.duplicate(nums3, duplication), "| duplication[0]=", duplication[0])
    print(u.duplicate(nums4, duplication), "| duplication[0]=", duplication[0])
    print(u.duplicate(nums5, duplication), "| duplication[0]=", duplication[0])
    print(u.duplicate(nums6, duplication), "| duplication[0]=", duplication[0])

    v = Solution1()
    print(v.duplicate(nums1))
    print(v.duplicate(nums2))
    print(v.duplicate(nums3))
    print(v.duplicate(nums4))
    print(v.duplicate(nums5))
    print(v.duplicate(nums6))
