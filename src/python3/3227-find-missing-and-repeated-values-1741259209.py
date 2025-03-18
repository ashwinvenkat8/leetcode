class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        
        expected_sum = (n**2) * ((n**2) + 1) // 2
        expected_sum_of_squares = (n**2) * ((n**2) + 1) * (2 * (n**2) + 1) // 6
        actual_sum, actual_sum_of_squares = 0, 0

        for i in range(n):
            for j in range(n):
                actual_sum += grid[i][j]
                actual_sum_of_squares += grid[i][j] * grid[i][j]
        
        sum_diff = actual_sum - expected_sum
        sum_of_squares_diff = actual_sum_of_squares - expected_sum_of_squares
        sum_of_a_b = sum_of_squares_diff // sum_diff

        a = (sum_of_a_b + sum_diff) // 2
        b = (sum_of_a_b - sum_diff) // 2

        return [a,b]
