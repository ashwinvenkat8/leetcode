class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        universal_strings = []
        word1_letter_counts = {}
        word2_letter_counts = {}
        words2_len = len(words2)
        
        for word in words2:
            for letter in word:
                word2_letter_counts[letter] = max(word2_letter_counts.get(letter, 0), word.count(letter))
        
        for word1 in words1:
            word1_letter_counts = {
                letter: word1.count(letter) for letter in word1
            }
            is_present = True
            
            for letter, count in word2_letter_counts.items():
                if letter not in word1_letter_counts or count > word1_letter_counts[letter]:
                    is_present = False
                    break
            
            # presence_count = 0
            # for word2 in words2:
            #     is_present = True
                
            #     for letter, count in word2_letter_counts[word2].items():
            #         if letter not in word1_letter_counts or count > word1_letter_counts[letter]:
            #             is_present = False
            #             break
                
            #     if is_present:
            #         presence_count += 1
            
            # if presence_count == words2_len:
            #     universal_strings.append(word1)
            
            if is_present:
                universal_strings.append(word1)
        
        return universal_strings
