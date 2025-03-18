class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        i, j = 1, len(nums)-1
        count = 1

        while i <= j:
            if nums[i] == nums[i-1]:
                nums.append(nums.pop(i))
                j -= 1
            else:
                count += 1
                i += 1
        
        return count
