class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""

        for s in strs:
            # Use length + delimiter pattern to handle any characters (including the delimiter itself)
            string += str(len(s)) + "#" + s
        
        return string
            

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        
        while i < len(s):
            # Find the delimiter to get the length
            j = s.find("#", i)
            length = int(s[i:j])
            # Extract the exact substring based on the length
            strs.append(s[j+1:j+1+length])
            i = j + 1 + length

        return strs