'''
题目描述
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置,
如果没有则返回 -1（需要区分大小写）.（从0开始计数）
示例1
输入  "google"
返回值 4
'''
class Solution:
    # 哈希表。时间复杂度O(n)，空间复杂度O(n)。这道题要求返回下标。
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1
        n = len(s)
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        for i in range(n):
            if d[s[i]] == 1:
                return i
        return -1

if __name__ == '__main__':
    u = Solution()
    s1 = ''
    s2 = 'google'
    print(u.FirstNotRepeatingChar(s1))
    print(u.FirstNotRepeatingChar(s2))