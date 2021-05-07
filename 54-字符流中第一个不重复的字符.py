'''
题目描述
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
后台会用以下方式调用Insert 和 FirstAppearingOnce 函数
string caseout = "";
1.读入测试用例字符串casein
2.如果对应语言有Init()函数的话，执行Init() 函数
3.循环遍历字符串里的每一个字符ch {
Insert(ch);
caseout += FirstAppearingOnce()
}
2. 输出caseout，进行比较。
返回值描述:
如果当前字符流没有存在出现一次的字符，返回#字符。
'''


class Solution:
    def __init__(self):
        self.s = ''
        self.dic = {}

    def FirstAppearingOnce(self):
        for key in self.s:
            if self.dic[key] == 1:
                return key
        return '#'

    def Insert(self, char):
        self.s += char
        if char not in self.dic:
            self.dic[char] = 1
        else:
            self.dic[char] += 1


if __name__ == '__main__':
    u = Solution()
    u.Insert('a')
    u.Insert('a')
    u.Insert('b')
    print(u.FirstAppearingOnce())
