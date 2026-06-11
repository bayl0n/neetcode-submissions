class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        seen = set()

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def isValid(r, c):
            return min(r, c) >= 0 and r < len(grid) and c < len(grid[0]) and grid[r][c] != "0"

        def dfs(r, c):
            if not isValid(r,c) or (r,c) in seen:
                return

            seen.add((r,c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in seen:
                    count += 1
                    dfs(i, j)

        return count