class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        count = 0
        freq = [0] * n
        result = [0] * n
        
        for i in range(n):
            freq[A[i]-1] += 1
            if freq[A[i]-1] == 2:
                count += 1
            freq[B[i]-1] += 1
            if freq[B[i]-1] == 2:
                count += 1
            result[i] = count
        
        return result
