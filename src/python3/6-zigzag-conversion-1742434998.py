class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        converted_s = ''
        row, col, row_dir, col_dir = 0, 0, -1, 1
        rail_matrix = []

        for r in range(numRows):
            rail_matrix.append([])
            for c in range(len(s)):
                rail_matrix[r].append('-')

        for ch in s:
            rail_matrix[row][col] = ch
            
            if row == 0 or row == numRows-1:
                row_dir *= -1
                col_dir = 1 - col_dir
            
            row += row_dir
            col += col_dir
        
        for r in range(numRows):
            for c in range(len(s)):
                if rail_matrix[r][c] != '-':
                    converted_s += rail_matrix[r][c]
        
        return converted_s
