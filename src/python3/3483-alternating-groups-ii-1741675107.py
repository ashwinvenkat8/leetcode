class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int: 
        n, count, l = len(colors), 0, 0

        for r in range(n + k - 1):
            if r > 0 and colors[r % n] == colors[(r - 1) % n]:
                l = r
            
            if r - l + 1 >= k:
                count += 1
        
        return count
