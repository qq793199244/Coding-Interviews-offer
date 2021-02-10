'''
题目描述
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
示例1
输入{8,6,10,5,7,9,11}
返回值[[8],[6,10],[5,7,9,11]]
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        res = []
        queue = [pRoot]
        while queue:
            tmp = []
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res


if __name__ == '__main__':
    u = Solution()
    root = TreeNode(8)
    n6 = root.left = TreeNode(6)
    n10 = root.right = TreeNode(10)
    n5 = n6.left = TreeNode(5)
    n7 = n6.right = TreeNode(7)
    n9 = n10.left = TreeNode(9)
    n11 = n10.right = TreeNode(11)
    print(u.Print(root))