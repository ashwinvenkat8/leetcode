class Solution:
    def isHappy(self, n: int) -> bool:
        def get_squared_sum(num):
            sum = 0
            while num:
                digit = num % 10
                sum += digit**2
                num //= 10
            return sum
        
        slow = get_squared_sum(n)
        fast = get_squared_sum((get_squared_sum(n)))
        
        while slow != fast:
            if fast == 1:
                return True
            slow = get_squared_sum(slow)
            fast = get_squared_sum((get_squared_sum(fast)))

        return slow == 1