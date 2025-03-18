class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n, m = len(nums1), len(nums2)
        i, j = 0, 0
        result = []

        while i < n and j < m:
            idx1, val1 = nums1[i][0], nums1[i][1]
            idx2, val2 = nums2[j][0], nums2[j][1]
            
            if idx1 == idx2:
                result.append([idx1, val1 + val2])
                i += 1
                j += 1
            elif idx1 < idx2:
                result.append([idx1, val1])
                i += 1
            else:
                result.append([idx2, val2])
                j += 1
        
        while i < n:
            result.append([nums1[i][0], nums1[i][1]])
            i += 1
        
        while j < m:
            result.append([nums2[j][0], nums2[j][1]])
            j += 1
        
        return result
