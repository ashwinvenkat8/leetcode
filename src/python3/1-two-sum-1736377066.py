class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i, num in enumerate(nums):
            for j in range(i+1, n):
                if num + nums[j] == target:
                    return [i, j]
        return