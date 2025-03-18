class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        merged_str = ''
        
        while i < len(word1) and i < len(word2):
            merged_str = ''.join([merged_str, word1[i], word2[i]])
            i += 1
        
        merged_str = ''.join([merged_str, word1[i:]])
        merged_str = ''.join([merged_str, word2[i:]])
        
        return merged_str