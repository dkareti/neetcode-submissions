class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """Determine if a sudoku board is valid."""
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key will be (r_idx // 3, c_idx // 3)
        dimension = 9

        for r_idx in range(dimension):
            for c_idx in range(dimension):
                if board[r_idx][c_idx] == ".":
                    continue
                if (
                    board[r_idx][c_idx] in rows[r_idx] or
                    board[r_idx][c_idx] in cols[c_idx] or
                    board[r_idx][c_idx] in squares[(r_idx // 3, c_idx // 3)]
                ):
                    return False
                rows[r_idx].add(board[r_idx][c_idx])
                cols[c_idx].add(board[r_idx][c_idx])
                squares[(r_idx // 3, c_idx // 3)].add(board[r_idx][c_idx])
        
        return True

