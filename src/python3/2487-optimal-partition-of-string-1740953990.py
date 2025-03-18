class Solution:
    def partitionString(self, s: str) -> int:
        unique_substring = []
        result = 1

        for char in s:
            if char in unique_substring:
                result += 1
                unique_substring = [char]
            else:
                unique_substring += [char]
        
        return result
