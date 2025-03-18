class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            i, carry = len(digits)-1, 0
            while i >= 0:
                if digits[i] == 9:
                    carry = 1
                    digits[i] = 0
                    i -= 1
                else:
                    break
            if i < 0:
                digits.insert(0,carry)
            else:
                digits[i] += carry
            return digits