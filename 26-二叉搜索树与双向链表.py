'''
题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''


'''
算法流程：
dfs(cur): 递归法中序遍历；
1. 终止条件： 当节点 curcur 为空，代表越过叶节点，直接返回；
2. 递归左子树，即 dfs(cur.left) ；
3. 构建链表：
    1.当 pre 为空时： 代表正在访问链表头节点，记为 head 。
    2.当 pre 不为空时： 修改双向节点引用，即 pre.right = curpre.right=cur ， cur.left = precur.left=pre ；
    3.保存 cur ： 更新 pre=cur ，即节点 cur 是后继节点的 pre ；
4. 递归右子树，即 dfs(cur.left) ；

特例处理： 若节点 root 为空，则直接返回；
初始化： 空节点 pre ；
转化为双向链表： 调用 dfs(root) ；
构建循环链表： 中序遍历完成后，head 指向头节点， pre 指向尾节点，因此修改 head 和 pre 的双向节点引用即可。
返回值： 返回链表的头节点 head 即可。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 时间复杂度O(n)；空间复杂度O(H)，最坏O(n)
    def Convert(self, pRootOfTree):
        def dfs(cur):
            if not cur: return
            dfs(cur.left)
            if self.pre:
                self.pre.right, cur.left = cur, self.pre
            else:   # 记录头节点
                self.head = cur
            self.pre = cur
            dfs(cur.right)

        if not pRootOfTree: return
        self.pre = None
        dfs(pRootOfTree)
        return self.head

if __name__ == '__main__':
    u = Solution()
    n4 = TreeNode(4)
    n2 = n4.left = TreeNode(2)
    n5 = n4.right = TreeNode(5)
    n1 = n2.left = TreeNode(1)
    n3 = n2.right = TreeNode(3)
    print(u.Convert(n4))
