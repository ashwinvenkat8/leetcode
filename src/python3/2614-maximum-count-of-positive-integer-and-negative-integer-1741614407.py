class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        if nums[0] > 0 or nums[-1] < 0:
            return len(nums)
        
        neg = bisect_left(nums, 0)
        pos = len(nums) - bisect_right(nums, 0)
        
        return max(neg, pos)
