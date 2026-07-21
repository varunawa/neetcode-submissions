class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #sort each individual part into alphabetical order and see if it matches with anything else
        sorted_words = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word not in sorted_words:
                sorted_words[sorted_word] = []
            sorted_words[sorted_word].append(word)
        
        return list(sorted_words.values())