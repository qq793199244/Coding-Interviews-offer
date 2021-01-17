'''
题目描述
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
对于50%的数据,size <= 10^4
对于75%的数据,size <= 10^5
对于100%的数据,size <= 2*10^5
输入描述:
题目保证输入的数组中没有的相同的数字
示例1
输入  [1,2,3,4,5,6,7,0]
返回值     7
'''
class Solution:
    def InversePairs(self, data):
        self.count = 0
        def merge(left, right):
            l, r = 0, 0
            tmp = []
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    tmp.append(left[l])
                    l += 1
                else:
                    self.count += (len(left) - l)
                    if self.count > 1000000007:
                        self.count %= 1000000007
                    tmp.append(right[r])
                    r += 1
            tmp += left[l:]
            tmp += right[r:]
            return tmp
        def merge_sort(arr):
            n = len(arr)
            if n <= 1: return arr
            mid = n // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)
        merge_sort(data)
        return self.count

if __name__ == '__main__':
    u = Solution()
    data1 = []
    data2 = [1,2,3,4,5,6,7,0]
    print(u.InversePairs(data1))
    print(u.InversePairs(data2))