'''
题目描述
输入两个链表，找出它们的第一个公共结点。
（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 双指针。时间复杂度O(m+n)，空间复杂度O(1)
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None
        cur1, cur2 = pHead1, pHead2
        while cur1 != cur2:
            cur1 = cur1.next if cur1 else pHead2
            cur2 = cur2.next if cur2 else pHead1
        return cur1


if __name__ == '__main__':
    u = Solution()
    n_common1 = ListNode(5)
    n_common2 = ListNode(100)
    # 1→2→5→4→100
    pHead1 = ListNode(1)
    n2 = pHead1.next = ListNode(2)
    n3 = n2.next = n_common1
    n4 = n3.next = ListNode(4)
    n100 = n4.next = n_common2

    # 9→8→11→5→12→100
    pHead2 = ListNode(9)
    n8 = pHead2.next = ListNode(8)
    n11 = n8.next = ListNode(11)
    n5 = n11.next = n_common1
    n12 = n5.next = ListNode(12)
    n100_2 = n12.next = n_common2

    print(u.FindFirstCommonNode(pHead1, pHead2))
    print(u.FindFirstCommonNode(pHead1, pHead2).val)
