class Queue:
    def __init__(self):
        self.list = []
        
    def __str__(self):
        values = [str(x) for x in self.list]
        return " ".join(values)
        
        
        
    def isEmpty(self):
        if self.list == []:
            return True
        return False
    
    def enQueue(self, value):
        return self.list.append(value)
    
    
    def deQueue(self):
        if self.isEmpty():
            print("The list is alredy empty")
        else:
            return self.list.pop(0)
        
    def peek(self):
        if self.isEmpty():
            print("There are no element to return")
        else:
            return self.list[0]
        
    def delete(self):
        self.list = []
        return 
        
    
    
        
        
que = Queue()
que.enQueue(34)
que.enQueue(534)
que.enQueue(3344)
que.enQueue(1244)
que.deQueue()
que.deQueue()
print(que)
print("==================")