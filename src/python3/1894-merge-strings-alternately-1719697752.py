class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        merged_str = []
        
        while i < min(len(word1), len(word2)):
            merged_str.append(word1[i])
            merged_str.append(word2[i])
            i += 1
        
        merged_str.append(word1[i:])
        merged_str.append(word2[i:])
        
        return ''.join(merged_str)