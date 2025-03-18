class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        isAnagram = False
        if set(s) == set(t) and len(s) == len(t):
            char_dict = {}
            for ch in s:
                char_dict[ch] = char_dict.get(ch, 0) + 1
            for ch in t:
                char_dict[ch] = char_dict.get(ch, 0) - 1
            for key in char_dict.keys():
                if char_dict[key] != 0:
                    isAnagram = False
                else:
                    isAnagram = True
        return isAnagram