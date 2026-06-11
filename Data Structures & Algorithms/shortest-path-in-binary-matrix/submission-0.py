class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        seen = set()

        directions = [
            (1,1),
            (-1,-1),
            (1,-1),
            (-1,1),
            (0,-1),
            (0,1),
            (-1,0),
            (1,0),
        ]

        queue = deque()

        queue.append((0, 0, 1))
        shortest_path = math.inf

        while queue:
            r, c, count = queue.popleft()

            # base case
            if min(r,c) < 0 or max(r,c) >= len(grid) or grid[r][c] != 0:
                continue

            seen.add((r,c))

            if r == len(grid) - 1 and c == len(grid) - 1:
                shortest_path = min(shortest_path, count)

            for dr, dc in directions:
                if (r+dr, c+dc) not in seen:
                    queue.append((r+dr, c+dc, count + 1))

        if shortest_path != math.inf:
            return int(shortest_path)
        else:
            return -1
            