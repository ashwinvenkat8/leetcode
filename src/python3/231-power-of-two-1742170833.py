class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0:
            for i in range(32):
                if 2**i == n:
                    return True
        return False