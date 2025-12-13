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
        
    
    
sll = SingleLinkedList()
node1 = Node(12)
node2 = Node(14)
node3 = Node(17)
sll.head = node1 #type: ignore
node1.next = node2 #type: ignore
node2.next = node3 #type: ignore
values = [node.data for node in sll]

print(values)
        