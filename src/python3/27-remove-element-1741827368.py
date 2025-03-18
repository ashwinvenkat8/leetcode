class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1
        count = 0

        while i <= j:
            if nums[i] == val:
                nums.append(nums.pop(i))
                j -= 1
            else:
                count += 1
                i += 1
        
        return count
