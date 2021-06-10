class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            temp = self.root
            while temp.next:
                temp = temp.next
            new_node = Node(data)
            temp.next = new_node

    def display(self):
        temp = self.root
        while temp:
            print(temp.data, end = " ")
            temp = temp.next

    def find_lenght(self):
        temp = self.root
        count = 0
        while temp:
            temp = temp.next
            count += 1
        return count

    def exchange_k_from_start_and_end(self, k):
        size = self.find_lenght()
        swap_index = (size - k) + 1
        prev_x = None
        count_x = 1
        current_x = self.root
        while current_x and count_x != k:
            prev_x = current_x
            current_x = current_x.next
            count_x += 1

        count_y = 1
        current_y = self.root
        prev_y = None
        while current_y and count_y != swap_index:
            prev_y = current_y
            current_y = current_y.next
            count_y += 1
        
        if not current_x or not current_y:
            return

        if prev_x:
            prev_x.next = current_y
        else:
            self.root = current_y

        if prev_y:
            prev_y.next = current_x
        else:
            self.root = current_x
        temp = current_y.next
        current_y.next = current_x.next
        current_x.next = temp

        self.display()

ll = LinkList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
# ll.display()
print(ll.exchange_k_from_start_and_end(5))