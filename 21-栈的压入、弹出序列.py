'''
题目描述
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
示例1
输入  [1,2,3,4,5],[4,3,5,1,2]
返回值 false
'''


class Solution:
    # 辅助栈模拟。时间复杂度O(n)，空间复杂度O(n)
    def IsPopOrder(self, pushV, popV):
        tmp_stack = []
        i = 0
        for num in pushV:
            # num入栈
            tmp_stack.append(num)
            # 当栈不为空 且 栈顶元素等于popV中的第i个元素
            while tmp_stack and tmp_stack[-1] == popV[i]:
                # 出栈
                tmp_stack.pop()
                # 移动指针
                i += 1
        # 若栈为空，返回True；不为空，返回False
        return not tmp_stack


if __name__ == '__main__':
    u = Solution()
    pushV1 = [1, 2, 3, 4, 5]
    popV1 = [4, 3, 5, 1, 2]
    popV2 = [5, 4, 3, 2, 1]
    print(u.IsPopOrder(pushV1, popV1))
    print(u.IsPopOrder(pushV1, popV2))
