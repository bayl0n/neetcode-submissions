class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # rows
        for row in range(9):
            dups = set()
            for col in range(9):
                if board[row][col] != ".":
                    if board[row][col] in dups:
                        return False
                    else:
                        dups.add(board[row][col])

        # cols
        for row in range(9):
            dups = set()
            for col in range(9):
                if board[col][row] != ".":
                    if board[col][row] in dups:
                        return False
                    else:
                        dups.add(board[col][row])

        # 3x3
        for grid_row in range(0, 9, 3):
            for grid_col in range(0, 9, 3):
                dups = set()

                for row in range(3):
                    for col in range(3):
                        if board[grid_row+row][grid_col+col] != ".":
                            if board[grid_row+row][grid_col+col] in dups:
                                return False
                            else:
                                dups.add(board[grid_row+row][grid_col+col])
        return True