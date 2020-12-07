'''
题目描述
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
示例1
输入{67,0,24,58}
返回值[58,24,0,67]
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printListFromTailToHead(self, listNode):
        if not listNode: return []
        res = []
        tmp = []
        while listNode:
            tmp.append(listNode.val)
            listNode = listNode.next
        while tmp:
            res.append(tmp.pop())
        return res


if __name__ == '__main__':
    u = Solution()
    h = ListNode(67)
    n0 = h.next = ListNode(0)
    n24 = n0.next = ListNode(24)
    n58 = n24.next = ListNode(58)
    print(u.printListFromTailToHead(h))