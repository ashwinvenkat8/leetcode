class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counts = {}
        result = []

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for num, count in counts.items():
            if count == 1:
                result.append(num)
        
        return result