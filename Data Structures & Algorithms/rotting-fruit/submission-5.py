class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        min_minutes = math.inf

        def isValid(r, c) -> bool:
            return min(r,c) >= 0 and r < len(grid) and c < len(grid[0])
            

        def hasFreshFruits() -> bool:
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] == 1:
                        return True
            return False

        def findRottenFruits():
            rotten_fruits = []
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] == 2:
                        rotten_fruits.append((row,col,0))

            return rotten_fruits

        rotten_fruits = findRottenFruits()

        queue = deque(rotten_fruits)
        seen = set()

        if not queue and not hasFreshFruits():
            return 0

        while queue:
            r, c, minutes = queue.popleft()

            if not isValid(r, c) or grid[r][c] == 0:
                continue

            seen.add((r,c))

            if grid[r][c] == 1:
                grid[r][c] = 2

            if not hasFreshFruits():
                min_minutes = min(min_minutes, minutes)

            for dr, dc in directions:
                if isValid(r+dr,c+dc) and (r+dr,c+dc) not in seen:
                    queue.append((r + dr, c + dc, minutes+1))

        if hasFreshFruits():
            return -1

        return int(min_minutes) if min_minutes != math.inf else -1