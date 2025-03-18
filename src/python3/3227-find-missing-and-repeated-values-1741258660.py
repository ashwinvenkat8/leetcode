class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        nums = dict.fromkeys([i for i in range(1,(n**2)+1)], 0)
        missing, twice = 0, 0

        for i in range(n):
            for j in range(n):
                nums[grid[i][j]] += 1
        
        for num, count in nums.items():
            if count == 0:
                missing = num
            if count == 2:
                twice = num
        
        return [twice, missing]
