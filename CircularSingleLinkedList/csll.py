class Node:
    def __init__(self, data) -> None:
        self.data: int = data  
        self.next: 'Node | None' = None
        
class CircularSingleLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        
    def __iter__(self):
        if self.head is None:
            return
        
        node: Node | None = self.head
        while True:
            if node is None:
                break
            yield node
            node = node.next
            if node == self.head:
                break
            
    def create_csll(self, data):
        node = Node(data)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL is created successfully"
    
    def insert(self, position, data):
        new_node = Node(data)
        if position == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                if self.tail is not None:
                    self.tail.next = self.head
        else:
            node = self.head
            index = 0
            while index < position - 1 and node is not None:
                node = node.next
                index += 1
            if node is not None:
                new_node.next = node.next
                node.next = new_node
            
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            if self.tail is not None:
                self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
            
    def remove(self, position):
        if self.head is None:
            print("There are no node to delete")
            return
            
        if position == 0:
            if self.head == self.tail:  # Only one node
                self.head.next = None
                self.head = None
                self.tail = None
            else:  # Multiple nodes
                removed_node = self.head
                self.head = self.head.next
                if self.tail is not None:
                    self.tail.next = self.head
                removed_node.next = None
        else:
            node = self.head
            index = 0
            while index < position - 1 and node is not None:
                node = node.next
                index += 1
            if node is not None and node.next is not None:
                next_node = node.next
                node.next = next_node.next
                next_node.next = None
            
            # Update tail if we removed the last node
            if next_node == self.tail:
                self.tail = node
                
    def pop(self):
        if self.head is None:
            return None
            
        # If only one node
        if self.head == self.tail:
            node = self.head
            self.head = None
            self.tail = None
            return node
            
        # Find second-to-last node
        current_node = self.head
        while current_node is not None and current_node.next != self.tail:
            current_node = current_node.next
            
        # Remove and return the tail
        node_to_remove = self.tail
        self.tail = current_node
        if self.tail is not None:
            self.tail.next = self.head
        return node_to_remove
        
    def display(self):
        if self.head is None:
            return "Empty list"
        values = [str(node.data) for node in self]
        return " -> ".join(values) + " -> (back to head)"
    
    def find_value(self, value):
        node = self.head
        if node is None:
            return "The value are not present in the list"
        else:
            while node:
                if node.data == value:
                    return node.data
                node = node.next
                if self.tail is not None and node == self.tail.next: 
                    return "The value are not present in the list"
                


# Test the corrected code
csll = CircularSingleLinkedList()
csll.insert(0, 142)
csll.insert(0, 134)
csll.insert(0, 5343)
csll.insert(1, 6433)
csll.insert(3, 9433)

print(csll.display())
print(csll.find_value(142))
print(csll.find_value(6433))
