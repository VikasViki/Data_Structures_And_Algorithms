class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class linked_list:

    def __init__(self):
        self.head = None
        self.last_node = None
    
    def insert_data(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
    
    def traverse_list(self):
        current = self.head
        while current:
            print(current.data,end=" ")
            current = current.next

s_link_list = linked_list()
no_of_nodes = int(input("Enter the Number of elements to add : "))
for i in range(no_of_nodes):
    data = int(input("Enter Data Item : "))
    s_link_list.insert_data(data)
print("The Linked List : ", end = " ")
s_link_list.traverse_list()
print()