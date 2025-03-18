class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n, a, b = len(grid), 0, 0
        nums = []

        for i in range(n):
            for j in range(n):
                nums.append(grid[i][j])
        
        for num in nums:
            if nums.count(num) == 2:
                a = num
        
        for i in range(1, (n**2)+1):
            if i not in nums:
                b = i
        
        return [a, b]
