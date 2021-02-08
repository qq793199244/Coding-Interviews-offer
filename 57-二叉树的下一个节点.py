'''
题目描述
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # 时间复杂度最坏O(n)，空间复杂度O(1)
    def GetNext(self, pNode):
        if pNode is None:
            return None
        # 此节点有右子树
        if pNode.right:
            tmp = pNode.right
            while tmp.left:
                tmp = tmp.left
            return tmp
        # 此节点无右子树
        while pNode.next:
            father = pNode.next
            if pNode == father.left:
                return father
            pNode = father
        return None


if __name__ == '__main__':
    u = Solution()
    root = TreeNode(1)
    n2 = root.left = TreeNode(2)
    n3 = root.right = TreeNode(3)
    n2.next = root
    n3.next = root
    print(u.GetNext(root))
    print(u.GetNext(root).val)

    print(u.GetNext(n2))
    print(u.GetNext(n2).val)