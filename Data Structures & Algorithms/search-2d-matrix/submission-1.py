class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find the correct row to perform binary search on
        ROWS, COLS = len(matrix), len(matrix[0])

        top = ROWS - 1
        bot = 0

        while bot <= top:
            row = (top + bot) // 2

            if target > matrix[row][-1]:
                bot = row + 1
            elif target < matrix[row][0]:
                top = row - 1
            else:
                break

        if not (bot <= top):
            return False

        row = (top + bot) // 2

        left = 0
        right = COLS - 1

        # Once the correct row is found, perform binary search
        while left <= right:
            col = (right + left) // 2

            if target > matrix[row][col]:
                left = col + 1
            elif target < matrix[row][col]:
                right = col - 1
            else:
                return True

        return False
