'''
题目描述
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
例如
[[a,b,c,e],
 [s,f,c,s],
 [a,d,e,e]]
矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
示例1
输入[[a,b,c,e],[s,f,c,s],[a,d,e,e]],"abcced"
返回值true
示例2
输入[[a,b,c,e],[s,f,c,s],[a,d,e,e]],"abcb"
返回值false
备注:
0 <= matrix.length <= 200
0 <= matrix[i].length <= 200
'''


class Solution:
    def hasPath(self, matrix, words):
        # @param matrix char字符型二维数组
        # @param word string字符串
        # @return bool布尔型
        def dfs(i, j, k):
            if not 0 <= i < len(matrix) or not 0 <= j < len(matrix[0]) or matrix[i][j] != words[k]:
                return False
            if k == len(words) - 1: return True
            matrix[i][j] = ''
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or \
                  dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            matrix[i][j] = words[k]
            return res

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if dfs(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    u = Solution()
    m1 = [["a", "b", "c", "e"], ["s", "f", "c", "s"], ["a", "d", "e", "e"]]
    w1 = "abcced"
    print(u.hasPath(m1, w1))

    m2 = [["a", "b", "c", "e"], ["s", "f", "c", "s"], ["a", "d", "e", "e"]]
    w2 = "abcb"
    print(u.hasPath(m2, w2))
