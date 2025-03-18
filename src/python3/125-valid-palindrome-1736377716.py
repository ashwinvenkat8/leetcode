from re import sub

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = sub(r'[^a-zA-Z0-9]', '', s.strip().lower())
        
        if not s_clean:
            return True
        
        i, j = 0, len(s_clean)-1
        while i < j:
            if s_clean[i] != s_clean[j]:
                return False
            i += 1
            j -= 1
        
        return True