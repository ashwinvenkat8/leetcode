class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0:
            while n % 2 == 0:
                n //= 2
            return n == 1
        return False