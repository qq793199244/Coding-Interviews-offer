'''
题目描述
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
示例1
输入      {5,4,#,3,#,2,#,1}
返回值     [5,4,3,2,1]
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        res = []
        tmp_queue = [root]
        while tmp_queue:
            node = tmp_queue.pop(0)
            res.append(node.val)
            if node.left:
                tmp_queue.append(node.left)
            if node.right:
                tmp_queue.append(node.right)
        return res


if __name__ == '__main__':
    u = Solution()
    root = TreeNode(5)
    n4 = root.left = TreeNode(4)
    n3 = n4.left = TreeNode(3)
    n2 = n3.right = TreeNode(2)
    n1 = n2.right = TreeNode(1)
    print(u.PrintFromTopToBottom(root))
