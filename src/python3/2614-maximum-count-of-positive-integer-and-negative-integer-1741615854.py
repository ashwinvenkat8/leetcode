class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        if nums[0] > 0 or nums[-1] < 0:
            return len(nums)
        
        l, h = 0, len(nums)
        while l < h:
            m = (l + h) // 2

            if nums[m] < 0:
                l = m + 1
            else:
                h = m
        n = l
        
        l, h = 0, len(nums)
        while l < h:
            m = (l + h) // 2

            if nums[m] <= 0:
                l = m + 1
            else:
                h = m
        p = len(nums) - l
        
        return max(n, p)
