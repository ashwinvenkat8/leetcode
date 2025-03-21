class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(set(height)) == 1:
            return (len(height)-1)*height[0]

        i, j = 0, len(height) - 1
        max_area = 0

        while i < j:
            curr_area = (j - i) * min(height[i], height[j])

            if curr_area > max_area:
                max_area = curr_area
            
            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1
        
        return max_area
