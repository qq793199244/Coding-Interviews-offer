'''
题目描述
给定一棵二叉搜索树，请找出其中的第k小的结点。
示例1
输入{5,3,7,2,4,6,8},3
返回值{4}
说明
按结点数值大小顺序第三小结点的值为4
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 中序遍历。时间复杂度O(n)，空间复杂度O(n)
class Solution:
    def KthNode(self, pRoot, k):
        if not pRoot or k <= 0:
            return None
        arr = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node)
            inorder(node.right)
        inorder(pRoot)
        if len(arr) < k:
            return None
        return arr[k - 1]


if __name__ == '__main__':
    u = Solution()
    root = TreeNode(5)
    n3 = root.left = TreeNode(3)
    n7 = root.right = TreeNode(7)
    n2 = n3.left = TreeNode(2)
    n4 = n3.right = TreeNode(4)
    n6 = n7.left = TreeNode(6)
    n8 = n7.right = TreeNode(8)
    print(u.KthNode(root, 3).val)



