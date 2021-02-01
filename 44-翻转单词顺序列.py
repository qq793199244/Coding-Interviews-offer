'''
题目描述
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。
同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。
例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。
Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
示例1
输入  "nowcoder. a am I"
返回值 "I am a nowcoder."
'''


class Solution:
    # 双指针。时间复杂度O(n)，空间复杂度O(n)
    # 1.倒序遍历字符串 s ，记录单词左右索引边界 i , j ；
    # 2.每确定一个单词的边界，则将其添加至单词列表 res ；
    # 3.最终，将单词列表拼接为字符串，并返回即可。
    def ReverseSentence1(self, s):
        s = s.strip()  # 删除首尾空格
        n = len(s)
        i = j = n - 1
        res = []
        while i >= 0:
            # 搜索首个空格
            while i >= 0 and s[i] != ' ':
                i -= 1
            res.append(s[i + 1: j + 1])
            # 跳过空格
            while s[i] == ' ':
                i -= 1
            # j指向下一个单词的尾字符
            j = i
        return ' '.join(res)

    # 分割+倒序。面试时不建议用。时间复杂度O(n)，空间复杂度O(n)
    def ReverseSentence2(self, s):
        s = s.strip()  # 删除首尾空格
        strs = s.split()  # 分割字符串
        strs.reverse()  # 翻转单词列表
        return ' '.join(strs)


if __name__ == '__main__':
    u = Solution()
    s1 = ""
    s2 = " "
    s3 = "nowcoder. a am I"
    s4 = "student. a am I"
    print(u.ReverseSentence1(s1))
    print(u.ReverseSentence1(s2))
    print(u.ReverseSentence1(s3))
    print(u.ReverseSentence1(s4))

    print(u.ReverseSentence2(s1))
    print(u.ReverseSentence2(s2))
    print(u.ReverseSentence2(s3))
    print(u.ReverseSentence2(s4))
