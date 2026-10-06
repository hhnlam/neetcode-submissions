class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        col = [0] * 9
        sqr = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.': continue
                val = int(board[r][c])

                bit = 1 << (val - 1)

                sqr_index = int((r // 3) * 3 + (c // 3))
                
                if rows[r] & bit or col[c] & bit or sqr[sqr_index] & bit: return False

                rows[r] |= bit
                col[c] |= bit
                sqr[sqr_index] |= bit
        return True