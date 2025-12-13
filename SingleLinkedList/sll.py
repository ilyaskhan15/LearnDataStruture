class Node:
    def __init__(self, Data):
        self.data = Data 
        self.next = None
        
class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next
        
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node #type: ignore
            self.tail = new_node
    
    def insert(self, position, data):
        new_node = Node(data)
        if position == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head #type: ignore
                self.head = new_node
        else:
            current_node = self.head
            index = 0
            while index < position -1:
                current_node = current_node.next #type: ignore
                index += 1
            next_node = current_node.next #type: ignore
            current_node.next = new_node #type: ignore
            new_node.next = next_node #type: ignore
            
    def pop(self):
        if self.head is None:
            print("There are no item to delete")
            return None
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                current_node = self.head
                while current_node.next != self.tail: #type: ignore
                    current_node = current_node.next #type: ignore
                data = self.tail.data #type: ignore
                self.tail = current_node
                self.tail.next = None #type: ignore
                return data
    
    
sll = SingleLinkedList()
sll.append(23)
sll.append(34)
sll.append(64)
sll.pop()
sll.pop()
sll.pop()
sll.pop()
values = [node.data for node in sll]
print(values)
        