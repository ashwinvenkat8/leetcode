class Solution:
    def hammingWeight(self, n: int) -> int:
        hamming_weight: int = 0
        while n > 0:
            hamming_weight += n % 2
            n = n >> 1
        return hamming_weight