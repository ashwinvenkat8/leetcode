class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        result = [0] * n
        
        for i in range(n):
            count = 0
            for j in range(i+1):
                if A[j] in B[:i+1]:
                    count += 1
            result[i] = count
        
        return result
