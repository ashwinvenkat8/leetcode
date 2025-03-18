class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        merged_str = []
        word1_len, word2_len = len(word1), len(word2)
        
        while i < word1_len and i < word2_len:
            merged_str.append(word1[i])
            merged_str.append(word2[i])
            i += 1
        
        merged_str.append(word1[i:])
        merged_str.append(word2[i:])
        
        return ''.join(merged_str)