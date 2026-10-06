class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dup_row = [[0] * 9 for _ in range(9)]
        dup_column = [[0] * 9 for _ in range(9)]
        dup_square = [[0] * 9 for _ in range(9)]
        for r, row in enumerate(board):
            for i, val in enumerate(row):
                if val == '.': continue
                val = int(val)

                dup_row[r][val-1] += 1
                if dup_row[r][val-1] > 1: return False

                dup_column[i][val-1] += 1
                if dup_column[i][val-1] > 1: return False

                sqr_index = int((r // 3) * 3 + (i // 3))
                dup_square[sqr_index][val-1] += 1
                if dup_square[sqr_index][val-1] > 1: return False
        return True
