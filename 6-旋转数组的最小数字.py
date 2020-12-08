'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
示例1
输入[3,4,5,1,2]
返回值1
'''
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        n = len(rotateArray)
        if n == 0: return 0
        left = 0
        right = n-1
        while left < right:
            mid = left + (right-left) // 2
            if rotateArray[mid] < rotateArray[right]:
                right = mid
            elif rotateArray[mid] > rotateArray[right]:
                left = mid + 1
            else:
                right -= 1
        return rotateArray[left]


if __name__ == '__main__':
    u = Solution()
    nums1 = [3, 4, 5, 1, 2]
    nums2 = [5, 1, 2, 3, 4]
    nums3 = [1, 0, 1, 1, 1]
    nums4 = [1, 1, 1, 0, 1]
    print(u.minNumberInRotateArray(nums1))
    print(u.minNumberInRotateArray(nums2))
    print(u.minNumberInRotateArray(nums3))
    print(u.minNumberInRotateArray(nums4))

'''
为什么官方的二分法的题解很多都是写的low + (high - low) // 2 而不是 (high + low) // 2
因为low+high在low和high特别大的时候可能会造成溢出，使用减法避免了溢出发生
但是Python3自动转换整数和长整数不需要考虑溢出，别的语言应该考虑一下
思想是这样
'''


