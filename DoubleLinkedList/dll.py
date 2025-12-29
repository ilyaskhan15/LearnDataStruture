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
                
    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                new_node.next = None
                new_node.pre = None
            else:
                new_node.next = self.head #type: ignore
                self.head.pre = new_node #type: ignore
                self.head = new_node
                new_node.pre = None
        elif position == -1:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                new_node.next = None
                new_node.pre = None
            else:
                new_node.pre = self.tail #type: ignore
                self.tail.next = new_node #type: ignore
                self.tail = new_node
                new_node.next = None
        else:
            current_node = self.head
            index: int = 0
            while index < position - 1 and current_node.next is not None:  #type: ignore
                current_node = current_node.next #type: ignore
                index += 1
            new_node.next = current_node.next #type: ignore
            new_node.pre = current_node #type: ignore
            new_node.next.pre = new_node #type: ignore
            current_node.next = new_node #type: ignore
        
    def triverse_forward(self):
        if self.tail is None:
            return "There are no data to trivers over"
        else:
            node = self.head
            while node:
                print(node.data)
                node = node.next
                
    def triverse_backward(self):
        if self.tail is None:
            return "There are no data to trivers over"
        else:
            node = self.tail
            while node:
                print(node.data)
                node = node.pre
    
    def search(self, data):
        if self.head is None:
            print("LinkedList is empty")
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.data == data: #type: ignore
                    return temp_node.data  #type: ignore  
                temp_node = temp_node.next  
            return "The value is not presnent in the list"
        
    def remove(self, position):
        if self.head is None:
            return "There is no elmeent to delete"
        else:
            if position == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.pre = None #type: ignore
            if position == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail= None
                else:
                    self.tail = self.tail.pre #type: ignore
                    self.tail.next = None #type: ignore
            else:
                temp_node = self.head
                index = 0
                while index < position - 1:
                    temp_node = temp_node.next #type: ignore
                    index += 1
                temp_node.next = temp_node.next.next #type: ignore
                temp_node.next.pre = temp_node #type: ignore
                
    def delete_entire_dll(self):
        if self.head is None:
            return "The list is alredy empty"
        else:
            temp_node = self.head
            while temp_node:
                temp_node.pre = None
                temp_node = temp_node.next
            self.head = None
            self.tail = None
            return "The Double linked list is been deleted successfully"
                
                
                
            

        
dll = DoubleLinkedList()
dll.insert(30, 0)
dll.insert(53, 0)
dll.insert(64, 0)
dll.insert(423, 1)
dll.insert(5343, 1)
dll.insert(5343, 4)
dll.remove(2)
print([node.data for node in dll])
print(dll.delete_entire_dll())
print([node.data for node in dll])
            
            