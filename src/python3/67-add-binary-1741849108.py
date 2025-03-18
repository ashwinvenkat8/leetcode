class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        i, j = len(a)-1, len(b)-1

        while i >= 0 or j >= 0:
            digit_a = ord(a[i]) - ord('0') if i >= 0 else 0
            digit_b = ord(b[j]) - ord('0') if j >= 0 else 0
            current_sum = digit_a + digit_b + carry
            result = str(current_sum % 2) + result
            carry = current_sum // 2
            i -= 1
            j -= 1
        
        if carry > 0:
            result = "1" + result
        
        return result