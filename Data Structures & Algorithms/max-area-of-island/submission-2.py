class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        max_count = 0

        directions = [
            (0,-1),
            (0,1),
            (-1,0),
            (1,0)
        ]

        def isValid(r, c):
            return (min(r,c) >= 0 and
                r < len(grid) and
                c < len(grid[0]) and
                grid[r][c] != 0)

        def dfs(r, c, total):
            if not isValid(r, c) or (r,c) in seen:
                return total

            seen.add((r,c))

            count = 0
            for dr, dc in directions:
                count += dfs(r + dr, c + dc, total)

            return 1 + count

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in seen:
                    max_count = max(max_count, dfs(i,j,0))

        return max_count

