'''
描述
输入一个长度为 n 整数数组，数组里面可能含有相同的元素，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前面部分，所有的偶数位于数组的后面部分，对奇数和奇数，偶数和偶数之间的相对位置不做要求，但是时间复杂度和空间复杂度必须如下要求。
数据范围：0≤n≤50000，数组中每个数的值0≤val≤10000
要求：时间复杂度 O(n)，空间复杂度 O(1)
示例1
输入：
[1,2,3,4]
返回值：
[1,3,2,4]
说明：
[3,1,2,4]或者[3,1,4,2]也是正确答案
示例2
输入：
[1,3,5,6,7]
返回值：
[1,3,5,7,6]
说明：
[3,1,5,7,6]等也是正确答案
示例3
输入：
[1,4,4,3]
返回值：
[1,3,4,4]
'''


class Solution:
    def reOrderArrayTwo(self, array):
        # write code here
        n = len(array)
        # 双指针
        left, right = 0, n - 1
        while left < right:
            # 跳过左边的奇数
            while left < right and array[left] % 2 == 1:
                left += 1
            # 跳过右边的偶数
            while left < right and array[right] % 2 == 0:
                right -= 1
            # 交换条件：左指针指的是偶数且右指针指的是奇数
            while left < right and array[left] % 2 == 0 and array[right] % 2 == 1:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        return array


if __name__ == '__main__':
    u = Solution()
    print(u.reOrderArrayTwo([1, 2, 3, 4]))  # [1,3,2,4]
    print(u.reOrderArrayTwo([1, 3, 5, 6, 7]))  # [1,3,5,7,6]
    print(u.reOrderArrayTwo([1, 4, 4, 3]))  # [1,3,4,4]
