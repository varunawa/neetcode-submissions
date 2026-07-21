class MinStack:
    # have two stacks: one the actual stack, and another to keep track of smallest

    def __init__(self):
        self.stack = []
        self.smallest = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.smallest or val <= self.smallest[-1]:
            self.smallest.append(val)
        else:
            self.smallest.append(self.smallest[-1])


    def pop(self) -> None:
        self.stack.pop()
        self.smallest.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.smallest[-1]
        
