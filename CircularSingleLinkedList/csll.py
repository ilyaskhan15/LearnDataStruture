class Node:
    def __init__(self, data) -> None:
        self.data = data  
        self.next = None
        
class CircularSingleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next
            
    def create_csll(self, data):
        node = Node(data)
        node.next = node #type: ignore
        self.head = node
        self.tail = node
        return "The CSLL is created successfully"
    
    def insert(self, position, data):
        new_node = Node(data)
        if position == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node #type: ignore
            else:
                new_node.next = self.head #type: ignore
                self.head = new_node
                self.tail.next = self.head #type: ignore
        else:
            node = self.head
            index = 0
            while index < position - 1:
                node = node.next #type: ignore
                index += 1
            new_node.next = node.next #type:ignore
            node.next = new_node #type: ignore
            
    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head #type: ignore
        else:
            self.tail.next = new_node #type: ignore
            new_node.next = self.head #type:ignore
            self.tail = new_node
        
        
csll = CircularSingleLinkedList()
csll.insert(0,142)
csll.insert(0,134)
csll.insert(0,5343)
csll.insert(1,6433)
csll.insert(3,9433)
csll.push(34)
csll.push(532)
csll.push(532)
csll.push(532)
values = [node.data for node in csll]
print(values)