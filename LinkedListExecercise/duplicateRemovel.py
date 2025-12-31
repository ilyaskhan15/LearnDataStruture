from linkedlist import LinkedList

def removeDuplicate(ll):
    if ll.head is None:
        return
    else:
        current_node = ll.head
        visited = set([current_node.value])
        while current_node.next:
            if current_node.next.value in visited:
                current_node.next = current_node.next.next
            else:
                visited.add(current_node.next.value)
                current_node = current_node.next
        return ll
    
    
    
    
    
ll = LinkedList()
ll.generator(10, 1, 9)
print(ll)
removeDuplicate(ll)
print(ll)