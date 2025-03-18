class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n, p = 0, 0

        for num in nums:
            if num < 0:
                n += 1
            if num > 0:
                p += 1
        
        return max(n, p)
