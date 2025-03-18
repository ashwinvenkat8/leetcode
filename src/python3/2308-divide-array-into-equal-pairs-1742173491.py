class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        num_counts = {}
        pairs = 0

        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1
        
        for num, count in num_counts.items():
            if count % 2 != 0:
                return False
        
        return True