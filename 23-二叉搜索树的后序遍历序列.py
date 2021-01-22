'''
题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则返回true,否则返回false。
假设输入的数组的任意两个数字都互不相同。
示例1
输入      [4,8,6,12,16,14,10]
返回值     true
'''


class Solution:
    # 递归。
    # 时间复杂度O(n^2)：每次递归去掉一个根节点，递归O(n)，每轮递归遍历树中节点O(n)
    # 空间复杂度O(H)，最坏O(n)
    def VerifySquenceOfBST(self, sequence):
        def recur(i, j):
            if i >= j:  # 终止条件：i >= j说明此子树节点数量 <= 1，无需判别正确性，直接返回 True
                return True
            p = i
            while sequence[p] < sequence[j]:
                p += 1
            m = p
            while sequence[p] > sequence[j]:
                p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(sequence) - 1)

    # 辅助单调栈。时间复杂度O(n)，空间复杂度O(n)
    def VerifySquenceOfBST2(self, sequence):
        tmp_stack, root = [], float('inf')
        for i in range(len(sequence) - 1, -1, -1):
            if sequence[i] > root:
                return False
            while tmp_stack and sequence[i] < tmp_stack[-1]:
                root = tmp_stack.pop()
            tmp_stack.append(sequence[i])
        return True


if __name__ == '__main__':
    u = Solution()
    s1 = []
    s2 = [4, 8, 6, 12, 16, 14, 10]
    s3 = [4, 6, 8, 10, 12, 14, 16]
    s4 = [16, 14, 10, 4, 8, 6, 12]

    print(u.VerifySquenceOfBST(s1))
    print(u.VerifySquenceOfBST(s2))
    print(u.VerifySquenceOfBST(s3))  # 一条链
    print(u.VerifySquenceOfBST(s4))

    print(u.VerifySquenceOfBST2(s1))
    print(u.VerifySquenceOfBST2(s2))
    print(u.VerifySquenceOfBST2(s3))  # 一条链
    print(u.VerifySquenceOfBST2(s4))
