class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # for each word, put the characters into separate array

        if s == None or t == None:
            return None

        s_chars = []
        t_chars = []

        for char in s:
            s_chars.append(char)

        for char in t:
            t_chars.append(char)
        
        s_chars.sort()
        t_chars.sort()

        if s_chars == t_chars:
            return True
        
        return False
