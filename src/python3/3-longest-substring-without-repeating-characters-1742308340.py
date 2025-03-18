class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n, i, j = 0, 0, 0
        char_set = set()

        while j < len(s):
            if s[j] not in char_set:
                char_set.add(s[j])
                n = max(n, j-i+1)
            else:
                while s[j] in char_set:
                    char_set.remove(s[i])
                    i += 1
                char_set.add(s[j])
            j += 1
        
        return n
