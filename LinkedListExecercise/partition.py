from linkedlist import LinkedList


def arrange(linkedlist, number):
    current_node = linkedlist.head
    linkedlist.tail = linkedlist.head
    
    while current_node:
        next_node = current_node.next
        current_node.next = None
        if current_node.value <= number:
            current_node.next = linkedlist.head
            linkedlist.head = current_node
        else:
            linkedlist.tail.next = current_node
            linkedlist.tail = current_node
        current_node = next_node
        
    if linkedlist.tail.next is not None:
        linkedlist.tail.next = None
            
            
ll = LinkedList()
ll.generator(10, 1, 10)
print(ll)
arrange(ll, 5)
print(ll)