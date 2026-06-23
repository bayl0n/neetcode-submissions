class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        The approach here is to have three separate hashmaps:
        - rows
        - cols
        - grids

        Then we are going to iterate through the grid three times and check each row, col and grid.
        If we see that the coordinate is already in the hashmap, then we can return false.

        If we successfully add each number in the hashmaps then we know that the answer is valid.
        """
        rows_dict = defaultdict(set)
        cols_dict = defaultdict(set)
        grids_dict = defaultdict(set)

        # rows
        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]

                if curr == ".":
                    continue

                if curr in rows_dict[i]:
                    return False
                else:
                    rows_dict[i].add(curr)

        # cols
        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]

                if curr == ".":
                    continue

                if curr in cols_dict[j]:
                    return False
                else:
                    cols_dict[j].add(curr)

        # grids
        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]

                if curr == ".":
                    continue

                if curr in grids_dict[(i // 3, j // 3)]:
                    return False
                else:
                    grids_dict[(i // 3, j // 3)].add(curr)

        return True