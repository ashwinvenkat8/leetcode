class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = []
        n, m = len(nums1), len(nums2)
        i, j = 0, 0

        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                merged_array.append(nums1[i])
                i += 1
            else:
                merged_array.append(nums2[j])
                j += 1
        
        while i < n:
            merged_array.append(nums1[i])
            i += 1
        while j < m:
            merged_array.append(nums2[j])
            j += 1
        
        n = len(merged_array)
        mid = n // 2
        
        if n % 2 == 0:
            return (merged_array[mid-1] + merged_array[mid]) / 2
        else:
            return merged_array[mid]
