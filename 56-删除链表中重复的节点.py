'''
题目描述
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
示例1
输入{1,2,3,3,4,4,5}
返回值{1,2,5}
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 时间复杂度O(n)，空间复杂度O(1)
    def deleteDuplication(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        if pHead.val == pHead.next.val:
            tmp = pHead.next
            while tmp and tmp.val == pHead.val:
                tmp = tmp.next
            return self.deleteDuplication(tmp)
        else:
            pHead.next = self.deleteDuplication(pHead.next)
            return pHead


if __name__ == '__main__':
    u = Solution()
    l1 = ListNode(1)
    l2 = l1.next = ListNode(2)
    l3_1 = l2.next = ListNode(3)
    l3_2 = l3_1.next = ListNode(3)
    l4_1 = l3_2.next = ListNode(4)
    l4_2 = l4_1.next = ListNode(4)
    l5 = l4_2.next = ListNode(5)
    res = u.deleteDuplication(l1)
    while res:
        print(res.val, end='→')
        res = res.next


