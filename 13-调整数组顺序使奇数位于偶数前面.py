'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''
class Solution:
    # 这个方法没有保证相对位置不变
    def reOrderArray(self, array):
        n = len(array)
        if n == 0: return []
        left = 0
        right = n-1
        while left < right:
            if array[left] % 2 != 0:
                left += 1
            elif array[right] % 2 == 0:
                right -= 1
            else:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        return array

    def reOrderArray2(self, array):
        odd_array =[]
        even_array = []
        n = len(array)
        if n == 0:
            return []
        for i in range(n):
            if array[i] % 2 == 0:
                even_array.append(array[i])
            else:
                odd_array.append(array[i])
        return odd_array + even_array



if __name__ == '__main__':
    u = Solution()
    array1 = [1, 2, 3, 4, 5, 6]
    array2 = [2, 4, 1, 3, 5]
    array3 = [1, 3, 5, 2, 4]
    print(u.reOrderArray(array1))
    print(u.reOrderArray2(array1))