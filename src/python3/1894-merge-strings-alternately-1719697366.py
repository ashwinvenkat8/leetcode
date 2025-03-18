class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        merged_str = ''
        word1_len, word2_len = len(word1), len(word2)
        
        while i < word1_len and i < word2_len:
            merged_str = ''.join([merged_str, word1[i], word2[i]])
            i += 1
        
        # if i < word1_len:
        merged_str = ''.join([merged_str, word1[i:]])
        # if i < word2_len:
        merged_str = ''.join([merged_str, word2[i:]])
        
        return merged_str