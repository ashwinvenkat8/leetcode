class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            bits, temp = 0, i
            while temp > 0:
                bits += int(temp % 2)
                temp /= 2
            result.append(bits)
        return result