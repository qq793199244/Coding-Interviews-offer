'''
题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
示例1
输入
[1,2,3,2,2,2,5,4,2]
返回值
2
'''


class Solution:
    # 哈希法
    def MoreThanHalfNum_Solution(self, numbers):
        n = len(numbers)
        d = {}
        for i in numbers:
            d[i] = d.get(i, 0) + 1
        # d_list = [[k, v] for k, v in d.items()]
        # for i in range(len(d_list)):
        #     if d_list[i][1] > n // 2:
        #         return d_list[i][0]
        # 同样的作用
        for key in d.keys():
            if d[key] > n//2:
                return key
        return 0


if __name__ == '__main__':
    u = Solution()
    nums1 = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(u.MoreThanHalfNum_Solution(nums1))
