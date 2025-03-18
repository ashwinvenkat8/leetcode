class Solution:
    def partitionString(self, s: str) -> int:
        unique_substring = set()
        result = 1

        for char in s:
            if char in unique_substring:
                result += 1
                unique_substring.clear()
            unique_substring.add(char)
        
        return result
