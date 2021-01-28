'''
题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则按字典序打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
示例1
输入      "ab"
返回值     ["ab","ba"]
'''


class Solution:
    def Permutation(self, ss):
        if ss == '':
            return []
        res = []

        def dfs(not_use, tmp):
            if not_use == '':
                res.append(tmp)
                return
            use_set = set()  # 记录当前位置之前已经使用过的字符
            for i in range(len(not_use)):
                ch = not_use[i]
                if ch in use_set:
                    continue
                else:
                    dfs(not_use[:i] + not_use[i + 1:], tmp + ch)
                    use_set.add(ch)

        dfs(ss, '')
        return res


if __name__ == '__main__':
    u = Solution()
    s1 = ""
    s2 = "ab"
    s3 = "abc"
    print(u.Permutation(s1))
    print(u.Permutation(s2))
    print(u.Permutation(s3))
