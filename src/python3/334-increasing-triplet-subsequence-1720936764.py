class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n1 = n2 = float('inf')
        for num in nums:
            if num > n2:
                return True
            if num > n1:
                n2 = min(num, n2)
            n1 = min(num, n1)
        return False