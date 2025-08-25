class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        row, col = 0, 0
        direction = 1  # 1 for up-right, -1 for down-left
        
        while len(result) < m * n:
            result.append(mat[row][col])
            
            if direction == 1:  # Up-right
                if col == n - 1:  # Hit right boundary
                    row += 1
                    direction = -1
                elif row == 0:  # Hit top boundary
                    col += 1
                    direction = -1
                else:  # Move up-right
                    row -= 1
                    col += 1
            else:  # Down-left
                if row == m - 1:  # Hit bottom boundary
                    col += 1
                    direction = 1
                elif col == 0:  # Hit left boundary
                    row += 1
                    direction = 1
                else:  # Move down-left
                    row += 1
                    col -= 1
        
        return result