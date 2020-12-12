'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
示例1
输入
{1,3,5},{2,4,6}
返回值
{1,2,3,4,5,6}
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def merge(self, pHead1, pHead2):
        if not pHead1 and not pHead2:
            return None
        cur = dummy = ListNode(0)
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                cur.next = pHead1
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                pHead2 = pHead2.next
            cur = cur.next
        if not pHead1:
            cur.next = pHead2
        if not pHead2:
           cur.next =  pHead1
        return dummy.next


if __name__ == '__main__':
    u = Solution()
    n1 = ListNode(1)
    n3 = n1.next = ListNode(3)
    n10 = n3.next = ListNode(10)
    n20 = n10.next = ListNode(20)

    l4 = ListNode(4)
    l5 = l4.next = ListNode(5)
    l6 = l5.next = ListNode(6)
    l7 = l6.next = ListNode(7)

    res = u.merge(n1, l4)
    while res:
        print(res.val, end='→')
        res = res.next

