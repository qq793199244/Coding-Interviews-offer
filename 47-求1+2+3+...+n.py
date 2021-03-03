'''
题目描述
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
示例1
输入5
返回值15
'''


class Solution:
    '''
    本题需要实现 “当 n = 1n=1 时终止递归” 的需求，可通过短路效应实现。
    n > 1 && sumNums(n - 1) // 当 n = 1 时 n > 1 不成立 ，此时 “短路” ，终止后续递归
    时间复杂度O(n)，空间复杂度O(n)
    '''
    def Sum_Solution(self, n):
        return n and (n + self.Sum_Solution(n - 1))


if __name__ == '__main__':
    u = Solution()

    print(u.Sum_Solution(0))
    print(u.Sum_Solution(1))
    print(u.Sum_Solution(5))
    print(u.Sum_Solution(100))
