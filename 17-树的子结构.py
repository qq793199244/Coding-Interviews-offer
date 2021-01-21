'''
题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。
（ps：我们约定空树不是任意一个树的子结构）
示例1
输入      {8,8,#,9,#,2,#,5},{8,9,#,2}
返回值     true
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    先找到B节点在A中的位置，由于A中可能有多个与B相同的值，所以要依次遍历；
    前序遍历；
    第二重递归里面，根据当前B节点的位置，继续递归左右子树，如果B递归完成，返回True；
    A递归完成，B未完成，或者值不相等，返回False
    时间复杂度O(mn)，空间复杂度O(m)，其中m为树A的节点数，n为树B的节点数
    '''
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return False
        if self.IsSubTree(pRoot1, pRoot2):
            return True
        else:
            return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def IsSubTree(self, tree1, tree2):
        if not tree2:
            return True
        if not tree1:
            return False
        if tree1.val == tree2.val:
            return self.IsSubTree(tree1.left, tree2.left) and self.IsSubTree(tree1.right, tree2.right)
        else:
            return False


if __name__ == '__main__':
    u = Solution()
    r1 = TreeNode(8)
    n8 = r1.left = TreeNode(8)
    n9 = n8.left = TreeNode(9)
    n2 = n9.left = TreeNode(2)
    n5 = n2.left = TreeNode(5)

    r2 = TreeNode(8)
    n9 = r2.left = TreeNode(9)
    n2 = n9.left = TreeNode(2)

    print(u.HasSubtree(r1, r2))
