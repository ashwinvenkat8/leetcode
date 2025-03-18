class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        prefix, postfix = 1, 1
        result = []

        for i in range(nums_len):
            result.append(prefix)
            prefix *= nums[i]
        
        for i in range(nums_len, 0, -1):
            result[i-1] *= postfix
            postfix *= nums[i-1]
        
        return result