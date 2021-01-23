'''
题目描述
输入一颗二叉树的根节点和一个整数，按字典序打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
示例1
输入{10,5,12,4,7},22
返回值 [[10,5,7],[10,12]]
示例2
输入{10,5,12,4,7},15
返回值 []
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归dfs。时间复杂度O(n)，空间复杂度O(Height)，当树退化到链表时，递归空间为O(n)
    def FindPath(self, root, expectNumber):
        res = []
        path = []

        def dfs(node, sum):
            # 递归出口：解决子问题
            if not node: return
            path.append(node.val)  # 将节点值添加到path
            sum -= node.val
            # 如果节点为叶子节点，并且 sum == 0
            if not node.left and not node.right and sum == 0:
                res.append(path[:])  # 注意Python的深拷贝和浅拷贝

            dfs(node.left, sum)
            dfs(node.right, sum)
            path.pop()  # 处理完一个节点后，恢复初始状态，为node.left,  node.right操作

        dfs(root, expectNumber)
        return res


if __name__ == '__main__':
    u = Solution()
    r1 = TreeNode(10)
    n5 = r1.left = TreeNode(5)
    n12 = r1.right = TreeNode(12)
    n4 = n5.left = TreeNode(4)
    n7 = n5.right = TreeNode(7)
    num1 = 22
    num2 = 15
    print(u.FindPath(r1, num1))
    print(u.FindPath(r1, num2))
