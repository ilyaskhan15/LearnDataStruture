from typing import Iterator, Optional

class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Optional["Node"] = None
        self.prev: Optional["Node"] = None


class CircularDoubleLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def __iter__(self) -> Iterator[Node]:
        if self.head is None:
            return iter(())

        node: Node = self.head
        assert node is not None
        while True:
            yield node
            next_node: Optional[Node] = node.next
            assert next_node is not None
            node = next_node
            if node == self.head:
                break

    def insert(self, data: int, position: int) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return
    
        if position == 0:
            new_node.next = self.head
            new_node.prev = self.tail
            assert self.head is not None
            assert self.tail is not None
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node
            return
    
        if position == -1:
            new_node.next = self.head
            new_node.prev = self.tail
            assert self.head is not None
            assert self.tail is not None
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node
            return
        
        current_node: Node = self.head
        index = 0
    
        while index < position - 1:
            assert current_node.next is not None
            if current_node.next == self.head:
                print(f"Position {position} is out of bounds")
                return
            current_node = current_node.next
            index += 1
        
        new_node.next = current_node.next
        new_node.prev = current_node
    
        assert new_node.next is not None
        new_node.next.prev = new_node
        
        current_node.next = new_node
    
        if new_node.next == self.head:
            self.tail = new_node
            
    def remove(self, position: int) -> None:
        if self.head is None:
            print("There are no element to delete")
        if position == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                assert self.head is not None
                assert self.tail is not None
                self.head = self.head.next
                assert self.head is not None
                self.tail.next = self.head
                self.head.prev = self.tail
        elif position == -1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                assert self.head is not None
                assert self.tail is not None
                self.tail = self.tail.prev
                assert self.tail is not None
                self.tail.next = self.head
                self.head.prev = self.tail
        else:
            temp_node: Optional[Node] = self.head
            assert temp_node is not None
            index = 0
            while index < position - 1:
                assert temp_node.next is not None
                temp_node = temp_node.next
                index += 1
            assert temp_node.next is not None
            temp_node.next = temp_node.next.next
            assert temp_node.next is not None
            temp_node.next.prev = temp_node
            
            
    def triverse_forward(self) -> None:
        if self.head is None:
            return
        
        current_node: Node = self.head
        assert current_node is not None
        while True:
            print(current_node.data)
            next_node: Optional[Node] = current_node.next
            assert next_node is not None
            current_node = next_node
            if current_node == self.head:
                break

    def triverse_backward(self) -> None:
        if self.tail is None:
            return
        
        current_node: Node = self.tail
        assert current_node is not None
        while True:
            print(current_node.data)
            prev_node: Optional[Node] = current_node.prev
            assert prev_node is not None
            current_node = prev_node
            if current_node == self.tail:
                break
            
    def search(self, data: int) -> None:
        if self.head is None:
            print("List is empty")
            return
        
        current_node: Optional[Node] = self.head
        assert current_node is not None
        while True:
            if current_node.data == data:
                print(f"Element {data} found")
                return
            next_node: Optional[Node] = current_node.next
            assert next_node is not None
            current_node = next_node
            if current_node == self.head:
                break
        print(f"Element {data} not found")


cdll = CircularDoubleLinkedList()
cdll.insert(34,0)
cdll.insert(34,0)
cdll.insert(100,-1)
cdll.insert(400,-1)
cdll.insert(400,1)
cdll.insert(3400,3)
cdll.remove(2)
cdll.remove(2)
numbers_list = [node.data for node in cdll]
cdll.triverse_forward()
print(numbers_list)
cdll.triverse_backward()
cdll.search(400)
