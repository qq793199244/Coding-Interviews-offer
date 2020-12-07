'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
示例1
输入[1,2,3,4,5,6,7],[3,2,4,1,6,5,7]
返回值{1,2,5,3,4,6,7}
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0: return None
        if len(pre) == 1: return TreeNode(pre)
        root = TreeNode(pre[0])
        pos = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:pos+1], tin[:pos])
        root.right = self.reConstructBinaryTree(pre[pos+1:], tin[pos+1:])
        return root
    # 层序遍历用于测试显示
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            length = len(queue)
            level = []
            for _ in range(length):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res


if __name__ == '__main__':
    u = Solution()
    pre = [1,2,3,4,5,6,7]
    tin = [3,2,4,1,6,5,7]
    print(u.levelOrder(u.reConstructBinaryTree(pre, tin)))

