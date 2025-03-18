class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = [1]

        for i in range(2, n+2):
            if n % i == 0:
                factors.append(i)
        
        if k-1 < len(factors):
            return factors[k-1]
        else:
            return -1