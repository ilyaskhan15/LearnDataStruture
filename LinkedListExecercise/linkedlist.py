from random import randint
from typing import Optional, Any

class Node:
    def __init__(self, value) -> None:
        self.value: int = value
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None
        
    def __str__(self):
        return str(self.value)
    
    
class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        
    def __iter__(self):
        current_node: Any = self.head
        while current_node:
            yield current_node
            current_node = current_node.next
            
    def __str__(self):
        values = [str(node.value) for node in self]
        return ' -> '.join(values)
            
    def __len__(self):
        result = 0
        current_node = self.head
        while current_node:
            result += 1
            current_node = current_node.next
        return result
        
        
    def add(self, value):
        new_node:Any = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node #type: ignore
            self.tail = new_node
        return self.tail
    
    def generator(self, numbers, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(numbers):
            self.add(randint(min_value, max_value))
        return self

    
    
    
