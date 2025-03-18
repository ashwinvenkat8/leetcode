class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_dict = {}
        for index in range(len(nums)):
            complement = target - nums[index]
            if complement in num_index_dict:
                return [num_index_dict[complement], index]
            num_index_dict[nums[index]] = index