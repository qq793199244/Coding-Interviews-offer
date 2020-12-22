'''
输入一个链表，输出该链表中倒数第k个结点。
示例1
输入 1,{1,2,3,4,5}
返回值{5}
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if not head or k == 0:
            return None
        fast = slow = head
        # 快指针比慢指针先走k-1步
        for _ in range(k):
            # k大于链表长度的情况
            if not fast:
                return None
            fast = fast.next
        # 同时走
        while fast:
            fast = fast.next
            slow = slow.next
        return slow

    def FindKthToTail2(self, head, k):
        cur = head
        pre = head
        while cur:
            cur = cur.next
            k -= 1
            if k < 0:
                pre = pre.next
        if k > 0:
            return None
        else:
            return pre

if __name__ == '__main__':
    u = Solution()
    n1 = ListNode(1)
    n2 = n1.next = ListNode(2)
    n3 = n2.next = ListNode(3)
    n4 = n3.next = ListNode(4)
    n5 = n4.next = ListNode(5)
    print(u.FindKthToTail(n1, 5).val)
    print(u.FindKthToTail(n1, 1).val)
    print(u.FindKthToTail(n1, 6))
    print(u.FindKthToTail2(n1, 5).val)
    print(u.FindKthToTail2(n1, 1).val)
    print(u.FindKthToTail2(n1, 6))