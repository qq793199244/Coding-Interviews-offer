'''
题目描述
请实现一个函数，用来判断一棵二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
示例1
输入{8,6,6,5,7,7,5}
返回值true
示例2
输入{8,6,9,5,7,7,5}
返回值false
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True

        def dfs(left, right):
            # 递归的终止条件是两个节点都为空，或者两个节点中有一个为空，或者两个节点的值不相等
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(pRoot.left, pRoot.right)
