class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre = None
        
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next #type: ignore
    
    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.pre = self.tail #type: ignore
            self.tail.next = node #type: ignore
            self.tail = node
            
            

        
dll = DoubleLinkedList()
dll.push(23)
dll.push(353)
dll.push(365)
dll.push(23)
dll.push(23)
dll_list = [node.data for node in dll]
print(dll_list)
            