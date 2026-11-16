class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row = 0
        r_row = len(matrix) - 1
        target_row = -1
        while l_row <= r_row:
            search = (l_row + r_row) // 2
            if matrix[search][0] <= target <= matrix[search][-1]:
                target_row = search
                break
            elif matrix[search][0] < target:
                l_row = search + 1
            else:
                r_row = search - 1
        
        if target_row == -1: return False

        l_col = 0
        r_col = len(matrix[search]) - 1
        while l_col <= r_col:
            search = (l_col + r_col) // 2
            if matrix[target_row][search] == target: return True
            elif matrix[target_row][search] < target: l_col = search + 1
            elif matrix[target_row][search] > target: r_col = search - 1
        return False