class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        anagram_groups = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagram_groups:
                anagram_groups[sorted_s] += [s]
            else:
                anagram_groups[sorted_s] = [s]
        
        return list(anagram_groups.values())
