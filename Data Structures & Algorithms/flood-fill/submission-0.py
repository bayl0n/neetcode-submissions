class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque()

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        queue.append((sr, sc))

        starting_color = image[sr][sc]

        if starting_color == color:
            return image

        while queue:
            r, c = queue.popleft()

            # base cases
            if min(r, c) < 0 or r >= len(image) or c >= len(image[0]) or image[r][c] != starting_color:
                continue

            for dr, dc in directions:
                queue.append((r + dr, c + dc))

            # modify image
            image[r][c] = color

        return image



            

            


