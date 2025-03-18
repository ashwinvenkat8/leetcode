import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s.strip().lower())
        
        # Using Python built-in function
        return True if not s else ''.join(reversed(s)) == s
        
        # Without Python built-in function
        # if not s:
        #     return True
        # left = 0
        # right = len(s) - 1
        # while left < right:
        #     if s[left] != s[right]:
        #         return False
        #     left += 1
        #     right -= 1
        # return True