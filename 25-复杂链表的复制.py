'''
题目描述
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针random指向一个随机节点），
请对此链表进行深拷贝，并返回拷贝后的头结点。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
示例 1：
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]     输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
示例 2：
输入：head = [[1,1],[2,1]]     输出：[[1,1],[2,1]]
示例 3：
输入：head = [[3,null],[3,0],[3,null]]     输出：[[3,null],[3,0],[3,null]]
示例 4：
输入：head = []    输出：[]
解释：给定的链表为空（空指针），因此返回 null。
提示：
-10000 <= Node.val <= 10000
Node.random为空（null）或指向链表中的节点。
节点数目不超过 1000 。
'''


class RandomListNode:
    def __init__(self, x, next=None, random=None):
        self.label = x
        self.next = None
        self.random = None


import copy


class Solution:
    # 调用函数，不建议。
    def Clone1(self, pHead):
        return copy.deepcopy(pHead)

    # 递归。时间复杂度O(n)，空间复杂度O(n)
    def Clone2(self, pHead):
        if not pHead:
            return None
        new = RandomListNode(pHead.label)
        new.random = pHead.random
        new.next = self.Clone2(pHead.next)
        return new

    # 迭代。时间复杂度O(n)，空间复杂度O(1)
    def Clone3(self, pHead):
        if not pHead:
            return pHead
        cur = pHead
        # 1. 复制各节点，并构建拼接链表
        while cur:
            tmp = RandomListNode(cur.label)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        # 2. 构建各新节点的 random 指向
        cur = pHead
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 3. 拆分两链表
        cur = res = pHead.next
        pre = pHead
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None  # 单独处理原链表尾节点
        return res  # 返回新链表头节点



if __name__ == '__main__':
    u = Solution()

    # p1 = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    pHead1 = RandomListNode(7)
    n13 = RandomListNode(13)
    n11 = RandomListNode(13)
    n10 = RandomListNode(13)
    n1 = RandomListNode(13)
   

    # p4 = []
