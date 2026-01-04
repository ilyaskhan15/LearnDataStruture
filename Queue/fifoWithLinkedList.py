class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next
        
        
class Queue:
    def __init__(self) -> None:
        self.items = LinkedList()
        
        
    def __str__(self):
        values = [str(x.value) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.items.head is None:
            return True
        return False
        
    def enQueue(self, new_node):
        new_node = Node(new_node)
        if self.items.head is None:
            self.items.head = new_node #type: ignore
            self.items.tail = new_node #type: ignore
        else:
            self.items.tail.next = new_node #type: ignore
            self.items.tail = new_node #type: ignore
            
    def deQueue(self):
        if self.isEmpty():
            print("There are no element to remove")
        else:
            if self.items.head == self.items.tail:
                self.items.head = None
                self.items.tail = None
            else:
                self.items.head = self.items.head.next #type: ignore
            
            
    def peek(self):
        if self.isEmpty():
            return "There are no element to return"
        else:
            return self.items.head.value #type: ignore
        
    def delete(self):
        self.items.head = None
        self.items.tail = None
            
            
que = Queue()
que.enQueue(34)
que.enQueue(43)
que.enQueue(50)
que.enQueue(65)
que.deQueue()
que.deQueue()
print(que)
            
            

        