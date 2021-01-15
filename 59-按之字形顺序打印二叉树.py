'''
请实现一个函数按照之字形打印二叉树，
即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，
第三行按照从左到右的顺序打印，其他行以此类推。
示例1
输入{8,6,10,5,7,9,11}
返回值[[8],[10,6],[5,7,9,11]]
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
        cur_queue = [pRoot]
        while cur_queue:
            tmp = []
            for i in range(len(cur_queue)):
                node = cur_queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    cur_queue.append(node.left)
                if node.right:
                    cur_queue.append(node.right)
            res.append(tmp)
        for row in range(len(res)):
            if row % 2 != 0:
                res[row].reverse()
        return res

if __name__ == '__main__':
    u = Solution()
    pRoot = TreeNode(8)
    n6 = pRoot.left = TreeNode(6)
    n10 = pRoot.right = TreeNode(10)
    n5 = n6.left = TreeNode(5)
    n7 = n6.right = TreeNode(7)
    n9 = n10.left = TreeNode(9)
    n11 = n10.right = TreeNode(11)
    print(u.Print(pRoot))

