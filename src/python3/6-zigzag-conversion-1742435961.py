class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        converted_s = [''] * numRows
        idx, dir = 0, -1

        for ch in s:
            converted_s[idx] += ch

            if idx == 0 or idx == numRows-1:
                dir *= -1

            idx += dir
        
        return ''.join(converted_s)
