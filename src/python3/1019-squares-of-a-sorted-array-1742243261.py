class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        i, j = 0, len(nums)-1

        while i <= j:
            n1, n2 = nums[i]**2, nums[j]**2

            if n2 >= n1:
                result.insert(0, n2)
                j -= 1
            else:
                result.insert(0, n1)
                i += 1
        
        return result