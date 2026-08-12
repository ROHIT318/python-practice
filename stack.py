# Node creation, node to be pushed in or popped out
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self, size):
        self.SIZE = size
        self.top = -1
        # self.no_elements = 0
        self.head = None

    def is_empty(self):
        if self.top == -1:
            return 1
        return 0

    def is_full(self):
        if self.top == self.SIZE:
            return 1
        return 0

    def size(self):
        print(self.top+1)

    def peek(self):
        return self.head.value

    def push(self, value):
        new_node = Node(value)
        if self.top == -1:
            self.head = new_node
            self.top += 1
        elif self.top+1 == self.SIZE:
            print("Stack Overflow!")
        else:
            new_node.next = self.head
            self.head = new_node
            self.top += 1
        return

    def pop(self):
        if self.top == -1:
            print("Stack underflow!")
        else:
            curr_node = self.head
            popped_node = curr_node
            self.head = curr_node.next
            self.top -= 1
            print(popped_node.value)

    def display_stack(self):
        curr_node = self.head
        if self.top == -1:
            print("No elements in the list!")
        while curr_node is not None:
            print(curr_node.value, "\n", "|")
            curr_node = curr_node.next


if __name__ == "__main__":
    # st = Stack(4)
    # st.push(1)
    # st.push(2)
    # st.push(3)
    # st.push(4)
    # st.display_stack() # 4 | 3 | 2 | 1
    # st.size() # 4
    # st.push(4) # Stack Overflow!
    # st.pop() # 4
    # st.pop() # 3
    # st.pop() # 2
    # st.pop() # 1
    # st.pop() # Stack underflow!
    # st.size() # 0
    # st.display_stack() # No elements in the list!

    string = "tihoR"
    str_list = list(string)
    rev_str = ""
    st = Stack(len(string))
    for ele in str_list:
        st.push(ele)
    # rev_str += st.pop()
    st.pop() # R
    st.pop() # o
    st.pop() # h
    st.pop() # i
    st.pop() # t
    st.pop() # Stack underflow!
