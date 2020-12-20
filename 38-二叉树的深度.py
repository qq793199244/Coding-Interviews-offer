'''
题目描述
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
示例1
输入
{1,2,3,4,5,#,6,#,#,7}
返回值
4
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return max(left, right) + 1


if __name__ == '__main__':
    u = Solution()
    n1 = TreeNode(1)
    n2 = n1.left = TreeNode(2)
    n3 = n1.right = TreeNode(3)
    n4 = n2.left = TreeNode(4)
    n5 = n2.right = TreeNode(5)
    n6 = n3.right = TreeNode(6)
    n7 = n5.left = TreeNode(7)
    print(u.TreeDepth(n1))
