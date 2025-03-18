class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected, actual = (len(nums)*(len(nums)+1))//2, 0
        for i in nums:
            actual += i
        return expected - actual