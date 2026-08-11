# Linked List
class Node():

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None

    def insert_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next != None:
                last_node = last_node.next

            last_node.next = new_node

    def insert_node_at_position(self, value, position):
        counter = 0
        new_node = Node(value)
        pos_node = self.head
        while counter < position-2:
            pos_node = pos_node.next
            counter += 1
        new_node.next = pos_node.next
        pos_node.next = new_node
        # 1 3 4 5

    def insert_node_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_node_at_end(self, value):
        new_node = Node(value)
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

    def delete_at_beginning(self):
        if self.head is not None:
            self.head = self.head.next
        else:
            print("No nodes present.")

    def delete_at_end(self):
        second_last_node = self.head
        if second_last_node is not None:
            while second_last_node.next.next is not None:
                second_last_node = second_last_node.next
        second_last_node.next = None

    def delete_at_position(self, pos):
        counter = 1
        del_node = self.head
        while counter < pos-1:
            del_node = del_node.next
            counter += 1
        del_node.next = del_node.next.next

    def delete_by_value(self, value):
        del_node = self.head
        if del_node.value == value:
            self.head = self.head.next
            return
        while del_node.next.value != value:
            del_node = del_node.next
        del_node.next = del_node.next.next
        
    def search_by_value(self, value):
        cur_node = self.head
        counter = 0
        while cur_node is not None and cur_node.value != value:
            cur_node = cur_node.next
            counter += 1
        if cur_node is None:
            print("Value not found.")
            return
        print(f"Value present at {counter+1}")
        
    def display_node(self):
        display_node = self.head

        if display_node is None:
            print("None")
            return
        while display_node is not None:
            print(display_node.value, "-> ", end="")
            display_node = display_node.next

        print("None")

ll = LinkedList()
ll.insert_node(1)
ll.insert_node(3)
ll.insert_node(4)
ll.insert_node(7)
ll.insert_node_at_position(5, 2)
ll.insert_node_at_beginning(0)
ll.insert_node_at_end(9) # 0 -> 1 -> 5 -> 3 -> 4 -> 7 -> 9 -> None
ll.display_node()
ll.delete_at_beginning()
ll.delete_at_end()
ll.delete_at_position(3)
ll.delete_by_value(1)
ll.search_by_value(10) # Value not found.
ll.search_by_value(5) # Value present at 1
ll.search_by_value(7) # Value present at 3
ll.display_node() # 5 -> 4 -> 7 -> None
