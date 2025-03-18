class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        def get_squared_sum(num):
            sum = 0
            while num:
                digit = num % 10
                sum += digit**2
                num //= 10
            return sum
        
        while n not in seen:
            seen.add(n)
            n = get_squared_sum(n)
            if n == 1:
                return True

        return False