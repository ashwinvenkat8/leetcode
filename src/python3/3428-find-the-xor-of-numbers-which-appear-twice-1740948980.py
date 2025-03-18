class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        counts = {}
        result = 0

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for num, count in counts.items():
            if count == 2:
                result ^= num
        
        return result