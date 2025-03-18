class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        isAnagram = False
        if set(s) == set(t) and len(s) == len(t):
            s_dict = {}
            t_dict = {}
            for ch in s:
                s_dict[ch] = s_dict.get(ch, 0) + 1
            for ch in t:
                t_dict[ch] = t_dict.get(ch, 0) + 1
            for key in s_dict.keys():
                if s_dict[key] != t_dict[key]:
                    isAnagram = False
                    break
                else:
                    isAnagram = True
        return isAnagram