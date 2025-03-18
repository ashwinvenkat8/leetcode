class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        counts = set()
        result = 0

        for num in nums:
            if num in counts:
                result ^= num
            else:
                counts.add(num)
        
        return result