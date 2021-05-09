'''
题目描述
请实现两个函数，分别用来序列化和反序列化二叉树

二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来的二叉树可以持久保存。
序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，序列化的结果是一个字符串，
序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。

二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。

例如，我们可以把一个只有根节点为1的二叉树序列化为"1,"，然后通过自己的函数来解析回这个二叉树
示例1
输入{8,6,10,5,7,9,11}
返回值{8,6,10,5,7,9,11}
'''

# 本题与LeetCode中 剑指 Offer 37. 序列化二叉树 有细微区别。
# https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 序列化二叉树。时间复杂度O(n)，空间复杂度O(n)
    def Serialize(self, root):
        res = []
        queue = []
        if root:
            queue.append(root)
        while queue:
            for i in range(len(queue)):
                x = queue.pop(0)
                x_val = str(x.val) if x else '#'
                res.append(x_val)
                if x:
                    queue.append(x.left)
                    queue.append(x.right)
        return ','.join(res)

    # 反序列化。时间复杂度O(n)，空间复杂度O(n)
    def Deserialize(self, s):
        if not s:
            return None
        queue = s.split(',')
        root = TreeNode(int(queue[0]))
        pre_layer = [root]
        queue.pop(0)
        while queue:
            for i in range(len(pre_layer)):
                parent = pre_layer.pop(0)
                left_val = queue.pop(0)
                if left_val != '#':
                    left_node = TreeNode(int(left_val))
                    parent.left = left_node
                    pre_layer.append(left_node)
                right_val = queue.pop(0)
                if right_val != '#':
                    right_node = TreeNode(int(right_val))
                    parent.right = right_node
                    pre_layer.append(right_node)
        return root


if __name__ == '__main__':
    u = Solution()
    tree1 = TreeNode(8)
    n6 = tree1.left = TreeNode(6)
    n10 = tree1.right = TreeNode(10)
    n5 = n6.left = TreeNode(5)
    n7 = n6.right = TreeNode(7)
    n9 = n10.left = TreeNode(9)
    n11 = n10.right = TreeNode(11)

    s1 = u.Serialize(tree1)
    print(s1)  # 输出 [8, 6, 10, 5, 7, 9, 11]
    # 反序列化
    print(u.Serialize(u.Deserialize(s1)))
