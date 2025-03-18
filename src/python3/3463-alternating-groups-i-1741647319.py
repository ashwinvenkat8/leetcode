class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        l, m, r, count = 0, 1, 2, 0
        n = len(colors)

        while l < n:
            if colors[l] != colors[m] and colors[l] == colors[r]:
                count += 1
            l += 1
            m = (m + 1) % n
            r = (r + 1) % n
        
        return count