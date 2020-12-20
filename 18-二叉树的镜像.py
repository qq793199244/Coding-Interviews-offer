'''
题目描述
操作给定的二叉树，将其变换为源二叉树的镜像。
输入描述:
二叉树的镜像定义：源二叉树
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Mirror(self, root):
        if not root:
            return root
        left = self.Mirror(root.left)
        right = self.Mirror(root.right)
        root.left, root.right = right, left
        return root


if __name__ == '__main__':
    u = Solution()
    n8 = TreeNode(8)
    n6 = n8.left = TreeNode(6)
    n10 = n8.right = TreeNode(10)
    n5 = n6.left = TreeNode(5)
    n7 = n6.right = TreeNode(7)
    n9 = n10.left = TreeNode(9)
    n11 = n10.right = TreeNode(11)
