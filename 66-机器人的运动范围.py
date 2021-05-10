'''
题目描述
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。
请问该机器人能够达到多少个格子？
示例1
输入  5,10,10
返回值 21
'''


# DFS。时间复杂度O(mn)，空间复杂度O(mn)
class Solution1:
    def movingCount(self, threshold, rows, cols):
        visited = [[1] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if i // 10 + i % 10 + j // 10 + j % 10 <= threshold:
                    visited[i][j] = 0

        def dfs(x, y):
            if x < 0 or x >= rows or y < 0 or y >= cols or visited[x][y]:
                return 0
            visited[x][y] = 1
            return 1 + dfs(x + 1, y) + dfs(x, y + 1)

        return dfs(0, 0)


# BFS。时间复杂度O(mn)，空间复杂度O(mn)。在牛客网上不能通过-10,10,10，改天改。
class Solution2:
    def movingCount(self, threshold, rows, cols):
        visited = [[1] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if i // 10 + i % 10 + j // 10 + j % 10 <= threshold:
                    visited[i][j] = 0

        queue = [(0, 0)]
        res = 0
        while queue:
            x, y = queue.pop(0)
            res += 1
            for dx, dy in ((1, 0), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
        return res


if __name__ == '__main__':
    u1 = Solution1()
    print(u1.movingCount(5, 10, 10))
    print(u1.movingCount(-10, 10, 10))

    u2 = Solution2()
    print(u2.movingCount(5, 10, 10))
    print(u2.movingCount(-10, 10, 10))
