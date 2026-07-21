class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = "({["
        matching = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []

        for c in s:
            if c in open_brackets:
                stack.append(c)
            else: 
                if not stack:
                    return False
                
                popped_element = stack.pop()

                if popped_element != matching[c]:
                    return False
        
        return len(stack) == 0