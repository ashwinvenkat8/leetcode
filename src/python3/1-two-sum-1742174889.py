class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_map: dict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in visited_map:
                return [visited_map[diff], i]
            visited_map[num] = i
        return