'''
输入一个整数，输出该数32位二进制表示中1的个数。其中负数用补码表示。
示例1
输入10
返回值2
'''
class Solution:
    def NumberOf1(self, n):
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += 1
            n = n & (n-1)
        return count

if __name__ == '__main__':
    u = Solution()
    print(u.NumberOf1(10))
    print(u.NumberOf1(8))
    print(u.NumberOf1(1))