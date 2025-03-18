class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 1:
            return 1
        count: int = 0
        while n > 0:
            if n % 2 == 1:
                count += 1
            n = n >> 1
        return count