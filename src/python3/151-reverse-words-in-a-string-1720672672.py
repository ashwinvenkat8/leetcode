class Solution:
    def reverseWords(self, s: str) -> str:
        s_stripped = s.strip()
        reversed_s = []
        current_word = ""        
        for c in s:
            if c.isspace() and len(current_word) > 0:
                reversed_s.insert(0, current_word)
                current_word = ""
            elif not c.isspace():
                current_word += c
        if len(current_word) > 0:
            reversed_s.insert(0, current_word)
        return " ".join(reversed_s)