class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n, count = len(colors), 0

        for i in range(n):
            if colors[i] != colors[(i+1)%n] and colors[i] == colors[(i+2)%n]:
                count += 1
        
        return count