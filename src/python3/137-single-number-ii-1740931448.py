class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    #     if len(nums) == 1:
    #         return nums[0]
    #     result: int = 0
    #     for num in nums:
    #         result |= num
    #     return result
    def singleNumber(self, nums):
        ones = 0
        twos = 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones