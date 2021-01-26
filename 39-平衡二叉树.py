'''
题目描述
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
平衡二叉树（Balanced Binary Tree），具有以下性质：
它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。
示例1
输入  {1,2,3,4,5,6,7}
返回值 true
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 计算深度，递归。时间复杂度O(nlogn)，空间复杂度O(n)
    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True
        def depth(root):
            if not root:
                return 0
            return max(depth(root.left), depth(root.right)) + 1
        return abs(depth(pRoot.left) - depth(pRoot.right)) <= 1 and \
               self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    # 后序遍历 + 剪枝 (自底向上)。时间复杂度O(n)，空间复杂度O(n)
    def IsBalanced_Solution2(self, pRoot):
        def recur(root):
            if not root:    # root等于0时，该节点符合要求，返回其深度0，而不返回-1
                return 0
            # 用left，right记录root左右子节点的深度，避免遍历root时对左右节点的深度进行重复计算。
            left = recur(root.left) #left最开始的取值为0，从底朝上遍历，先左子树，后右子树，最后根节点
            if left == -1:  # 若出现节点的深度为-1，则进行剪枝，开始向上返回，之后的迭代不再进行
                return -1
            right = recur(root.right)
            if right == -1:
                return -1
            # 最开始计算的是左子树最左侧的一个叶节点，其左右子节点不存在，left=0，right=0，满足条件，返回该叶节点的深度max(0,0)+1=1
            if abs(left - right) <= 1:
                return max(left, right) + 1
            else:
                return -1
        return recur(pRoot) != -1



if __name__ == '__main__':
    u = Solution()
    n4 = TreeNode(4)
    n2 = n4.left = TreeNode(2)
    n6 = n4.right = TreeNode(6)
    n1 = n2.left = TreeNode(1)
    n3 = n2.right = TreeNode(3)
    n5 = n6.left = TreeNode(5)
    n7 = n6.right = TreeNode(7)
    print(u.IsBalanced_Solution(n4))
    print(u.IsBalanced_Solution2(n4))

    r1 = TreeNode(1)
    r2 = r1.left = TreeNode(2)
    r3 = r1.right = TreeNode(3)
    r4 = r2.left = TreeNode(4)
    r5 = r2.right = TreeNode(5)
    r6 = r5.left = TreeNode(6)
    print(u.IsBalanced_Solution(r1))
    print(u.IsBalanced_Solution2(r1))