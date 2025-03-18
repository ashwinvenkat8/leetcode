class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # count, pref_len = 0, len(pref)
        # for word in words:
        #     last_compared_index = -1
        #     if len(word) >= pref_len:
        #         for i in range(pref_len):
        #             if pref[i] != word[i]:
        #                 break
        #             last_compared_index = i
        #         if last_compared_index == (pref_len - 1):
        #             count += 1
        # return count
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1
        return count