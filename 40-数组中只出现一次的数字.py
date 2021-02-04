'''
题目描述
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''


class Solution:
    # 哈希表。时间复杂度O(n)，空间复杂度O(n)
    def FindNumsAppearOnce1(self, array):
        d = {}
        res = []
        for i in array:
            d[i] = d.get(i, 0) + 1
        for i in d:
            if d[i] == 1:
                res.append(i)
        return res

    # 异或。时间复杂度O(n)，空间复杂度O(1)
    def FindNumsAppearOnce2(self, array):
        '''
        数列中a，b只出现了一次，将所有数字异或，最终得到的是a，b的异或。
        对sum取负号，其实就是先取反再加一，与sum与之后得到最低位的bit 1。
        对数列中与bit位相同的数字进行异或，可得到a，b之一，res与sum异或得到另一个。
        '''
        sum_num, res = 0, 0
        for i in array:
            sum_num ^= i
        bit = sum_num & (-sum_num)
        for i in array:
            if bit & i:
                res ^= i
        return [res, res ^ sum_num]


if __name__ == '__main__':
    u = Solution()
    array = [1, 1, 2, 2, 3, 4, 4, 5, 6, 6]
    print(u.FindNumsAppearOnce1(array))
    print(u.FindNumsAppearOnce2(array))
