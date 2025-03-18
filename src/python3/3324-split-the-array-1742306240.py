class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        n = len(nums)

        if n % 2 != 0:
            return False
        
        for count in Counter(nums).values():
            if count > 2:
                return False
        
        return True