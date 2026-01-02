class Stack:
    def __init__(self):
        self.list: list = []
        
    def __str__(self):
        self.list.reverse()
        value = [str(x) for x in self.list]
        return '\n'.join(value)
    
    def isEmpty(self):
        if self.list == []:
            return True
        return False
    
    def push(self, value):
        return self.list.append(value)
    
    def pop(self):
        if self.isEmpty():
            return "There are no element to delete"
        else:
            return self.list.pop()
        
    def peek(self):
        if self.isEmpty():
            return "There to no thing to show"
        else:
            return self.list[0]
        
        
    def deleteFullStack(self):
        if self.isEmpty:
            print("There is no thing to delete")
        else:
            self.list = []
            return self.list
    
    
stack = Stack()
stack.push(43)
stack.push(53)
stack.push(65)
stack.push(53)
stack.push(88)
stack.push(85)
stack.push(905)
print(stack)
print(stack.peek())
