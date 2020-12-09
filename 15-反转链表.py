'''
输入一个链表，反转链表后，输出新链表的表头。
示例1
输入{1,2,3}
返回值{3,2,1}
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        pre = None
        cur = pHead
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre


if __name__ == '__main__':
    u = Solution()
    h = ListNode(1)
    n2 = h.next = ListNode(2)
    n3 = n2.next = ListNode(3)
    res = u.ReverseList(h)
    while res:
        print(res.val, end='→')
        res = res.next