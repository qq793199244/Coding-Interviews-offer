'''
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''
class Solution:
    # 时间复杂度O(n)，空间复杂度O(n)
    def replaceSpace(self, s):
        if not s:
            return s
        res = ''
        for i in s:
            if i == ' ':
                res += '%20'
            else:
                res += i
        return res

if __name__ == '__main__':
    u = Solution()
    s1 = 'We Are Happy'
    s2 = ''
    print(u.replaceSpace(s1))