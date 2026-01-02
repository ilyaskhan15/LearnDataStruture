class Stack:
    def __init__(self, max_size) -> None:
        self.max_size = max_size
        self.list = []
        
    def __str__(self):
        self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        return False
    
    def push(self, value):
        if len(self.list) < self.max_size:
            return self.list.append(value)
        else:
            print("Stack Overflow")
            
            
    def pop(self):
        if self.isEmpty():
            print("Stack underflow: There is no element to delete")
        else:
            self.list.pop()
            
    def peek(self):
        if self.isEmpty():
            print("There are no element to return")
        else:
            print(self.list[0])
            
    def delete(self):
        if self.isEmpty():
            print("There is no thing to delete")
        else:
            self.list = []
            return self.list
        
stack = Stack(10)
stack.push(34)
stack.push(54)
stack.push(23)
stack.push(433)

print(stack)
print("|||||||||||||||||||||||||||||||")
stack.delete()
print(stack)
print("|||||||||||||||||||||||||||||||")
stack.peek()
        