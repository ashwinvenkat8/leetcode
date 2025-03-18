class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        return len(nums) % 2 == 0 and all(count < 3 for count in Counter(nums).values())
