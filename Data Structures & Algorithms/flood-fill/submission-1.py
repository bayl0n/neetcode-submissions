class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        stack = []

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        stack.append((sr, sc))

        starting_color = image[sr][sc]

        if starting_color == color:
            return image

        while stack:
            r, c = stack.pop()

            # base cases
            if min(r, c) < 0 or r >= len(image) or c >= len(image[0]) or image[r][c] != starting_color:
                continue

            for dr, dc in directions:
                stack.append((r + dr, c + dc))

            # modify image
            image[r][c] = color

        return image



            

            


