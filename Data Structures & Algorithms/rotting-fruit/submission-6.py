class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        min_minutes = 0
        fresh = 0
        queue = deque()

        def isValid(r, c) -> bool:
            return min(r,c) >= 0 and r < len(grid) and c < len(grid[0])
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row,col))
                elif grid[row][col] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
    
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if isValid(nr,nc) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((r + dr, c + dc))
    
            min_minutes += 1


        return min_minutes if fresh == 0 else -1