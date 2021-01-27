'''
题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
'''


class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        self.stack.append(node)
        # 若最小栈为空，或node小于等于（避免了重复最小值被弹出）最小栈中的栈顶元素，则将node加入到最小栈
        if not self.min_stack or node <= self.min_stack[-1]:
            self.min_stack.append(node)
        return node

    def pop(self):
        s = self.stack.pop()
        if s == self.min_stack[-1]:
            self.min_stack.pop()
        return s

    def top(self):
        if self.stack:
            return self.stack[-1]

    def min(self):
        if self.min_stack:
            return self.min_stack[-1]


# 代码中多余的return是为了写用例时测试

if __name__ == '__main__':
    u = Solution()
    print('push:', u.push(1))
    print('push:', u.push(2))
    print('push:', u.push(1))
    print('push:', u.push(1))
    print('push:', u.push(3))
    print('push:', u.push(3))
    print('push done')
    print('top:', u.top())
    print('min:', u.min())
    print('pop:', u.pop())
    print('pop:', u.pop())
    print('pop:', u.pop())
    print('top:', u.top())
    print('min:', u.min())
