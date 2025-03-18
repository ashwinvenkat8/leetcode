class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        merged_str = []
        shortest_str_len = min(len(word1), len(word2))
        
        while i < shortest_str_len:
            merged_str.append(word1[i])
            merged_str.append(word2[i])
            i += 1
        
        merged_str.append(word1[i:])
        merged_str.append(word2[i:])
        
        return ''.join(merged_str)