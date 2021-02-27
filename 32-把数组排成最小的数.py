'''
题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
示例1
输入[3,32,321]
返回值"321323"
'''


class Solution:
    # 时间复杂度O(nlogn)，空间复杂度O(n)
    def PrintMinNumber(self, numbers):
        def quick_sort(l, r):
            if l >= r: return
            i, j = l, r
            while i < j:
                while strs[j] + strs[l] >= strs[l] + strs[j] and i < j: j -= 1
                while strs[i] + strs[l] <= strs[l] + strs[i] and i < j: i += 1
                strs[i], strs[j] = strs[j], strs[i]
            strs[i], strs[l] = strs[l], strs[i]
            quick_sort(l, i - 1)
            quick_sort(i + 1, r)

        strs = [str(num) for num in numbers]
        quick_sort(0, len(strs) - 1)
        return ''.join(strs)


if __name__ == '__main__':
    u = Solution()
    n1 = [3, 32, 321]
    print(u.PrintMinNumber(n1))