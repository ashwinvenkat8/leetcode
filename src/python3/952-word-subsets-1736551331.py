class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        universal_strings = []
        max_letter_counts = [0] * 26
        temp_letter_counts = [0] * 26
        
        for word in words2:
            for letter in word:
                temp_letter_counts[ord(letter)-ord('a')] += 1
            
            for i in range(26):
                max_letter_counts[i] = max(max_letter_counts[i], temp_letter_counts[i])
            
            temp_letter_counts = [0] * 26
        
        for word in words1:
            for letter in word:
                temp_letter_counts[ord(letter)-ord('a')] += 1
            
            is_present = True
            
            for i in range(26):
                if max_letter_counts[i] > temp_letter_counts[i]:
                    is_present = False
                    break
            
            if is_present:
                universal_strings.append(word)
            
            temp_letter_counts = [0] * 26
        
        return universal_strings