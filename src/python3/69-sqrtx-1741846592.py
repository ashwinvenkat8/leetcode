class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 1, x

        while l <= h:
            m = (l+h) // 2
            m_sq = m * m

            if m_sq == x:
                return m
            elif m_sq < x:
                l = m + 1
            else:
                h = m - 1
        
        return h