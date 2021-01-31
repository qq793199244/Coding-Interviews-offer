'''
题目描述
LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！
“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....
LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。
现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。
为了方便起见,你可以认为大小王是0。
示例1
输入  [0,3,2,6,4]
返回值 true
'''


class Solution:
    # 1. 除大小王外，无重复
    # 2. 除大小王外，max-min<5
    # 集合 + 遍历
    def IsContinuous1(self, numbers):
        if not numbers:  # 牛客网需要判断这个情况
            return False
        is_repeat = set()
        max_num, min_num = 0, 14
        for num in numbers:
            if num == 0:
                continue
            max_num = max(max_num, num)
            min_num = min(min_num, num)
            if num in is_repeat:  # 如果这个数在集合中出现过，说明重复了，直接return False
                return False
            is_repeat.add(num)  # 将这个数加入到集合
        return max_num - min_num < 5

    # 排序数组中相邻两元素相同，重复，返回False
    # 排序 + 遍历
    def IsContinuous2(self, numbers):
        if not numbers:
            return False
        king_nums = 0
        numbers.sort()
        for i in range(4): # 这里是4，因为后面要比较numbers[i] == numbers[i + 1]
            if numbers[i] == 0:
                king_nums += 1  # 大小王的数量
            elif numbers[i] == numbers[i + 1]:
                return False
        return numbers[4] - numbers[king_nums] < 5  # 0的数量 = 排序后数组非零数的下标


if __name__ == '__main__':
    u = Solution()
    nums1 = [0, 3, 2, 6, 4]
    nums2 = [1, 3, 5, 0, 0]
    nums3 = [1, 3, 5, 7, 9]
    nums4 = []
    print(u.IsContinuous1(nums1))
    print(u.IsContinuous1(nums2))
    print(u.IsContinuous1(nums3))
    print(u.IsContinuous1(nums4))

    print(u.IsContinuous2(nums1))
    print(u.IsContinuous2(nums2))
    print(u.IsContinuous2(nums3))
    print(u.IsContinuous2(nums4))
