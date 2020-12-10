'''
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 快慢指针。时间复杂度O(n) 空间复杂度O(1)
    def EntryNodeOfLoop(self, pHead):
        if not pHead or not pHead.next or not pHead.next.next:
            return None
        slow = fast = pHead
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast and fast == slow:
                fast = pHead
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None

    # 哈希表。时间复杂度O(n) 空间复杂度O(n)
    def EntryNodeOfLoop2(self, pHead):
        if not pHead or not pHead.next or not pHead.next.next:
            return None
        hash = set()
        while pHead:
            if pHead not in hash:
                hash.add(pHead)
                pHead = pHead.next
            else:
                return pHead



if __name__ == '__main__':
    u = Solution()
    p1 = ListNode(1)
    p2 = p1.next = ListNode(2)
    p3 = p2.next = ListNode(3)
    p4 = p3.next = ListNode(4)
    p4.next = p2

    l1 = ListNode(1)
    l2 = l1.next = ListNode(2)

    print(u.EntryNodeOfLoop(p1).val)
    print(u.EntryNodeOfLoop(l1))
    print(u.EntryNodeOfLoop2(p1).val)
    print(u.EntryNodeOfLoop2(l1))
