class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = str(n)

        while num not in seen:
            seen.add(num)
            sum = 0

            for digit in num:
                digit = int(digit)
                sum += digit**2
            
            if sum == 1:
                return True
            num = str(sum)
        
        return False