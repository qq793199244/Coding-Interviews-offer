'''
题目描述
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}；
针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
{[2,3,4],2,6,2,5,1}，
{2,[3,4,2],6,2,5,1}，
{2,3,[4,2,6],2,5,1}，
{2,3,4,[2,6,2],5,1}，
{2,3,4,2,[6,2,5],1}，
{2,3,4,2,6,[2,5,1]}。
窗口大于数组长度的时候，返回空
示例1
输入 [2,3,4,2,6,2,5,1],3
返回值 [4,4,6,6,6,5]
'''


class Solution:
    # 暴力法，面试时不要用。时间复杂度O(n*k)，空间复杂度O(n)
    def maxInWindows1(self, num, size):
        if size == 0:
            return []
        if size > len(num):
            return []
        else:
            res = []
            for i in range(len(num) - size + 1):
                res.append(max(num[i:i + size]))
            return res

    # 单调队列。时间复杂度O(n)，空间复杂度O(k)
    def maxInWindows2(self, nums, size):
        left, right = 1 - size, 0  # left指向窗口左端， right指向右端
        res = []
        queue = []
        while right < len(nums):
            queue.append(nums[right])
            while len(queue) >= 2 and queue[-2] < queue[-1]:
                queue.pop(-2)
            if left >= 0:
                res.append(queue[0])
            if queue[0] == nums[left]:
                queue.pop(0)  # 队列的左端要被移除窗口
            right += 1
            left += 1
        return res


if __name__ == '__main__':
    u = Solution()
    num1 = [2, 3, 4, 2, 6, 2, 5, 1]
    s1 = 3
    print(u.maxInWindows1(num1, s1))
    print(u.maxInWindows2(num1, s1))
    print(u.maxInWindows1(num1, 9))
    print(u.maxInWindows2(num1, 9))
