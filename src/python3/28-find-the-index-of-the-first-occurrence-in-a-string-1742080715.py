class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_len, needle_len = len(haystack), len(needle)
        
        for i in range(haystack_len):
            j = 0
            for k in range(i, haystack_len):
                if haystack[k] == needle[j]:
                    j += 1
                else:
                    break
                if j == needle_len:
                    return i

        return -1