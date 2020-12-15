'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
示例1
输入
[4,5,1,6,2,7,3,8],4
返回值
[1,2,3,4]
'''


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        n = len(tinput)
        if k > n:
            return []

        def adjustMaxHeap(arr, i, n):
            tmp = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and arr[left] > arr[tmp]:
                tmp = left
            if right < n and arr[right] > arr[tmp]:
                tmp = right
            if tmp != i:
                arr[tmp], arr[i] = arr[i], arr[tmp]
                adjustMaxHeap(arr, tmp, n)

        for i in range((n - 1) // 2, -1, -1):
            adjustMaxHeap(tinput, i, n)

        for i in range(n - 1, 0, -1):
            tinput[0], tinput[i] = tinput[i], tinput[0]
            adjustMaxHeap(tinput, 0, i)
        return tinput[:k]


if __name__ == '__main__':
    u = Solution()
    tinput1 = [4, 5, 1, 6, 2, 7, 3, 8]
    print(u.GetLeastNumbers_Solution(tinput1, 4))
