# Node class representing each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  
class SinglyLinkedList:
    def __init__(self):
        self.head = None  
    def append(self, data):
        new_node = Node(data) 
        if self.head is None:
            self.head = new_node  
        else:
            current = self.head
            while current.next:  
                current = current.next
            current.next = new_node  
    def get_last_element(self):
        if self.head is None:
            return None  
        current = self.head
        while current.next:  
            current = current.next
        return current.data 
    def is_last_element_multiple_of_3(self):
        last_element = self.get_last_element()
        if last_element is None:
            print("The list is empty.")
        elif last_element % 3 == 0:
            print(f"The last element {last_element} is a multiple of 3.")
        else:
            print(f"The last element {last_element} is not a multiple of 3.")
linked_list = SinglyLinkedList()
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(8)
linked_list.append(9)
last_element = linked_list.get_last_element()
print(f"The last element is: {last_element}")
linked_list.is_last_element_multiple_of_3()
