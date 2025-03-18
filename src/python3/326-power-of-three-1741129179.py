class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n > 0:
            for i in range(32):
                if 3**i == n:
                    return True
        return False