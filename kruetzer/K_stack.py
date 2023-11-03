class K_stack:
    def __init__(self):
        self.stack = []
        
    def push(self,val):
        if not val:
            raise ValueError("No input data")
        self.stack.append(val)
        
    def pop(self):
        self.stack.pop(0)
    def find(self,val):
        if not val:
            raise ValueError("No input data")
        idx = self.stack.index(val)
        if idx:
            return idx
        else:
            raise ValueError("No such number found")
    def minimum(self):
        return min(self.stack)
    def maximum(self):
        return max(self.stack)
    def display(self):
        output = "[ " + "  |  ".join(str(element) for element in self.stack) + " ]"
        print(output)
    
    