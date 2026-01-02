from typing import Optional
class Node:
    def __init__(self, data):
        self.data: int = data
        self.next = next
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next
            
        

class Stack:
    def __init__(self):
        self.linked_list = LinkedList()
        
    def __str__(self):
        values = [str(x.data) for x in self.linked_list]
        return '\n'.join(values)
        
    def isEmpty(self):
        if self.linked_list.head == None:
            return True
        return False
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.linked_list.head #type: ignore
        self.linked_list.head = new_node #type: ignore
        
    def pop(self):
        if self.isEmpty():
            return "There are no element to delete"
        else:
            temp_value = self.linked_list.head.data #type: ignore
            self.linked_list.head = self.linked_list.head.next #type: ignore
            return temp_value
        
    def peek(self):
        if self.isEmpty():
            return "There no element to return"
        else:
            return self.linked_list.head.data #type: ignore
        
    def delete(self):
        self.linked_list.head = None
            
            
        
        
stack = Stack()
stack.push(23)
stack.push(53)
stack.push(65)
print(stack)
print("==================")
print(stack.peek())
stack.delete()
print(stack)


        